from django.shortcuts import render, redirect
from django.views.generic import FormView, ListView, DetailView

from braces.views import LoginRequiredMixin

from .forms import PostCreateForm, TagCreateForm, CategoryCreateForm
from .models import Post, Comment

class CreatePost(LoginRequiredMixin, FormView):

	template_name = 'posts/create_post.html'
	login_url = '/user/'
	form_class = PostCreateForm
	success_url = '/'

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.save()
		return super(CreatePost, self).form_valid(form)


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