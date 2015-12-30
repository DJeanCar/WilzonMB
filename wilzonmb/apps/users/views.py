from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import FormView, TemplateView
from django.core.urlresolvers import reverse_lazy

from .forms import UserRegisterForm, UserLogInForm
from braces.views import AnonymousRequiredMixin

def LogOut(request):
	logout(request)
	return redirect('/')

class UserLoginView(AnonymousRequiredMixin, FormView):

	template_name = 'users/login.html'
	form_class = UserLogInForm
	authenticated_redirect_url = reverse_lazy("home")

	def form_valid(self, form):
		user = authenticate(
					username = form.cleaned_data['username'],
					password = form.cleaned_data['password']
				)
		if user.is_active:
			login(self.request, user)
			return redirect('/')
		else:
			return redirect('/no-activo/')

class UserRegisterView(FormView):

	template_name = 'users/user_register.html'
	form_class = UserRegisterForm
	success_url = '/'

	def form_valid(self, form):
		user = form.save()
		user.set_password(form.cleaned_data['password'])
		user.save()
		user = authenticate(
					username = form.cleaned_data['username'],
					password = form.cleaned_data['password']
				)
		if user.is_active:
			login(self.request, user)
		return super(UserRegisterView, self).form_valid(form)