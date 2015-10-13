from django.shortcuts import render
from django.views.generic import TemplateView

from apps.posts.models import Post

class IndexView(TemplateView):

	template_name = 'main/home.html'

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['posts'] = Post.objects.all().order_by('-created')
		return context