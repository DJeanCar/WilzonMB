#encoding=utf-8
from django import forms
from .models import User

class UserRegisterForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 
					'email', 'password')
		widgets = {
			'username' : forms.TextInput(attrs={
					'class' : 'input input-username',
					'required': True,
					'placeholder': 'Ingresa un nombre de usuario'
				}),
			'first_name' : forms.TextInput(attrs={
					'class' : 'input input-username',
					'required': True,
					'placeholder': 'Ingresa tus nombres'
				}),
			'last_name' : forms.TextInput(attrs={
					'class' : 'input input-username',
					'required': True,
					'placeholder': 'Ingresa tus apellidos'
				}),
			'email' : forms.TextInput(attrs={
					'class' : 'input input-email',
					'type' : 'email',
					'required': True,
					'placeholder': 'Ingresa un email'
				}),
			'password' : forms.TextInput(attrs={
					'class' : 'input',
					'type' : 'password',
					'required': True,
					'placeholder': 'Ingresa una contraseña'
				})
		}


class UserLogInForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('username', 'password')
		widgets = {
			'username' : forms.TextInput(attrs={
					'class' : 'input input-username',
					'required': True,
					'type': 'text',
					'placeholder': 'Ingresa tu nombre de usuario'
				}),
			'password' : forms.TextInput(attrs={
					'class' : 'input',
					'type' : 'password',
					'required': True,
					'placeholder': 'Ingresa tu contraseña'
				})
		}

	def clean(self):
		if not User.objects.filter(username = self.cleaned_data.get('username')).exists():
			self.add_error('username', 'El nombre de usuario no esta registrado')
		else:
			user = User.objects.get(username = self.cleaned_data.get('username'))
			if not user.check_password(self.cleaned_data.get('password')):
				self.add_error('username', 'La contraseña es incorrecta')