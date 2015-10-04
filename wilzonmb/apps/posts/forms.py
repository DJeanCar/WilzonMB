from django import forms

from .models import Post, Tag, Category

class PostCreateForm(forms.ModelForm):

	class Meta:
		model = Post
		exclude = ('slug','user')

class TagCreateForm(forms.ModelForm):

	class Meta:
		model = Tag
		exclude = ('slug', 'user')

class CategoryCreateForm(forms.ModelForm):

	class Meta:
		model = Category
		exclude = ('slug', 'user')