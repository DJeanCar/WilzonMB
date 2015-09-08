#encoding=utf-8
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import (
	AbstractBaseUser, BaseUserManager, PermissionsMixin
)

class UserManager(BaseUserManager, models.Manager):

	def _create_user(self, username, email, password, is_staff,
				is_superuser, **extra_fields):

		email = self.normalize_email(email)
		if not email:
			raise ValueError('El email debe ser obligatorio')
		user = self.model(username = username, email=email, is_active=True,
				is_staff = is_staff, is_superuser = is_superuser, **extra_fields)
		user.set_password(password)
		user.save( using = self._db)
		return user

	def create_user(self, username, email, password=None, **extra_fields):
		return self._create_user(username, email, password, False,
				False, **extra_fields)

	def create_superuser(self, username, email, password=None, **extra_fields):
		return self._create_user(username, email, password, True,
				True, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
	'''
		Modelo de Usuarios	
	'''

	username = models.CharField(max_length=30, unique=True, db_index=True, validators = [
				RegexValidator(
						regex = '^[a-zA-Z0-9]*$',
						message = 'Username Inválido'
					)
		])
	email = models.EmailField(max_length=100, unique = True)
	first_name = models.CharField(max_length=200, null=True , blank=True)
	last_name = models.CharField(max_length=200, null=True , blank = True)
		
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	created = models.DateTimeField(null=True, blank=True, auto_now_add=True)
	modified = models.DateTimeField(null=True, blank=True, auto_now=True)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	objects = UserManager()

	def get_full_name(self):
		return ('%s %s') % (self.first_name,self.last_name) 

	def get_short_name(self):
		return self.username

	def __unicode__(self):
		return self.username