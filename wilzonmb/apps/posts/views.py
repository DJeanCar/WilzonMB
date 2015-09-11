from django.shortcuts import render
from django.views.generic import FormView

from braces.views import LoginRequiredMixin

from .forms import PostCreateForm

class CreatePost(LoginRequiredMixin, FormView):

	template_name = 'posts/create_post.html'
	login_url = '/user/'
	form_class = PostCreateForm