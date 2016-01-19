from django.shortcuts import render, redirect
from django.views.generic import FormView, ListView, DetailView, UpdateView
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.contrib import messages
from django.db.models import Q

from braces.views import LoginRequiredMixin


from .forms import PostCreateForm, TagCreateForm, CategoryCreateForm
from .models import Post, Comment

class CreatePost(LoginRequiredMixin, FormView):

	template_name = 'posts/create_post.html'
	login_url = '/user/'
	form_class = PostCreateForm
	success_url = '/'

	def get_context_data(self, **kwargs):
		context = super(CreatePost, self).get_context_data(**kwargs)
		if self.request.session.get('saved'):
			messages.add_message(self.request, messages.SUCCESS, 'Se creo el post correctamente')
			self.request.session['saved'] = False
		return context

	def form_valid(self, form):
		form.instance.user = self.request.user
		post = form.save()
		if 'save' in self.request.POST:
			''' Grabar '''
			self.success_url = reverse('home')
		elif 'save2' in self.request.POST:
			''' Grabar y agregar otro '''
			self.request.session['saved'] = True
			self.success_url = reverse('create_post')
		else:
			''' Grabar y continuar editando '''
			self.request.session['saved'] = True
			self.success_url = reverse('edit_post', kwargs={'pk':post.id})
		return super(CreatePost, self).form_valid(form)

class EditPost(LoginRequiredMixin, UpdateView):

	form_class = PostCreateForm
	model = Post
	login_url = '/user/'
	template_name = 'posts/edit_post.html'
	success_url = '/'

	def get_context_data(self, **kwargs):
		context = super(EditPost, self).get_context_data(**kwargs)
		self.request.session['urlToReturn'] = self.request.META['HTTP_REFERER']
		if self.request.session.get('saved'):
			messages.add_message(self.request, messages.SUCCESS, 'Se creo el post correctamente')
			self.request.session['saved'] = False
		return context

	def form_valid(self, form):
		if 'save' in self.request.POST:
			''' Grabar '''
			self.success_url = self.request.session['urlToReturn']
			self.request.session['urlToReturn'] = None
		elif 'save2' in self.request.POST:
			''' Grabar y agregar otro '''
			self.success_url = reverse('create_post')
		else:
			''' Grabar y continuar editando '''
			self.success_url = reverse('edit_post', kwargs={'pk':self.object.id})
		return super(EditPost, self).form_valid(form)

class CreateTag(LoginRequiredMixin, FormView):

	template_name = 'posts/create_tag.html'
	login_url = '/user/'
	form_class = TagCreateForm
	success_url = '/tag/crear/'

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.save()
		return super(CreateTag, self).form_valid(form)

class CreateCategory(LoginRequiredMixin, FormView):

	template_name = 'posts/create_category.html'
	login_url = '/user/'
	form_class = CategoryCreateForm
	success_url = '/categoria/crear/'

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.save()
		return super(CreateCategory, self).form_valid(form)


class PostList(ListView):

	model = Post
	template_name = 'posts/post_list.html'
	context_object_name = 'posts'
	paginate_by = 3

	def get(self, request, *args, **kwargs):
		search_id = request.GET.get('search_id')
		search_title = request.GET.get('search_title')
		search_description = request.GET.get('search_description')
		search_category = request.GET.get('search_category')
		search_tag = request.GET.get('search_tag')
		self.results = None
		if search_id and search_title and search_description and search_category and search_tag:
			self.results = Post.objects.filter(Q(title__icontains=search_title) | Q(pk__icontains=search_id) | Q(description_short__icontains=search_description) | Q(category__title__icontains=search_category) | Q(tag__title__icontains=search_tag)).order_by('-created')
		elif search_id:
			self.results = Post.objects.filter(Q(pk__icontains=search_id)).order_by('-created')
		elif search_title:
			self.results = Post.objects.filter(Q(title__icontains=search_title)).order_by('-created')
		elif search_description:
			self.results = Post.objects.filter(Q(description_short__icontains=search_description)).order_by('-created')
		elif search_category:
			self.results = Post.objects.filter(Q(category__title__icontains=search_category)).order_by('-created')
		elif search_tag:
			self.results = Post.objects.filter(Q(tag__title__icontains=search_tag)).order_by('-created')
		elif search_title and search_category:
			self.results = Post.objects.filter(Q(title__icontains=search_title) | Q(category__title__icontains=search_tag)).order_by('-created')
		elif search_title and search_tag:
			self.results = Post.objects.filter(Q(title__icontains=search_title) | Q(tag__title__icontains=search_tag)).order_by('-created')
		elif search_title and search_tag and search_category:
			self.results = Post.objects.filter(Q(title__icontains=search_title) | Q(tag__title__icontains=search_tag) | Q(category__title__icontains=search_tag)).order_by('-created')
		elif search_description and search_category:
			self.results = Post.objects.filter(Q(description_short__icontains=search_title) | Q(category__title__icontains=search_tag)).order_by('-created')
		elif search_description and search_tag:
			self.results = Post.objects.filter(Q(description_short__icontains=search_title) | Q(tag__title__icontains=search_tag)).order_by('-created')
		elif search_description and search_tag and search_category:
			self.results = Post.objects.filter(Q(description_short__icontains=search_title) | Q(tag__title__icontains=search_tag) | Q(category__title__icontains=search_tag)).order_by('-created')
		else:
			pass
		return super(PostList, self).get(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(PostList, self).get_context_data(**kwargs)
		context['search'] = self.results
		return context

	def post(self, request, *args, **kwargs):
		"""
			Eliminar post seleccionados
		"""
		Post.objects.filter(id__in=request.POST.getlist('delete')).delete()
		return redirect(self.request.META['HTTP_REFERER'])

class PostDetail(DetailView):

	model = Post
	template_name = 'posts/post_detail.html'
	context_object_name = 'post'


	def get_context_data(self, **kwargs):
		context = super(PostDetail, self).get_context_data(**kwargs)
		context['comments'] = Comment.objects.filter(post = kwargs['object'])
		return context

	def post(self, request, *args, **kwargs):
		Comment.objects.create(
				user = request.user,
				post = Post.objects.get(slug = kwargs['slug']),
				description = request.POST['comment']
			)
		return redirect('/posts/%s/' % kwargs['slug'])