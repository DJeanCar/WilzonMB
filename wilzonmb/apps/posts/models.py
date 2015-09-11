from django.db import models
from django.template.defaultfilters import slugify

from apps.users.models import User
from ckeditor.fields import RichTextField

class Category(models.Model):

	user = models.ForeignKey(User)

	title = models.CharField(max_length = 50)
	slug = models.SlugField(max_length = 50)
	description_short = RichTextField()
	description_large = RichTextField()
	description_extra = models.TextField()
	status = models.BooleanField(default = True)
	orden = models.IntegerField()
	en_menu = models.BooleanField(default = True)
	en_breadcrumbs = models.BooleanField(default = True)
	meta_title = models.CharField(max_length = 50)
	meta_description = models.TextField()
	meta_keywords = models.CharField(max_length = 250)
	meta_author = models.CharField(max_length = 45)
	xmlsitemap = models.BooleanField(default = True)
	xmlsitemap_prioridad = models.CharField(max_length = 4)

	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)

	def __unicode__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		super(Movie, self).save(*args, **kwargs)


class Tag(models.Model):

	user = models.ForeignKey(User)

	title = models.CharField(max_length = 50)
	slug = models.SlugField(max_length = 50)
	status = models.BooleanField(default = True)
	description = models.TextField()
	orden = models.IntegerField()
	meta_title = models.CharField(max_length = 50)
	meta_description = models.TextField()
	meta_keywords = models.CharField(max_length = 250)
	meta_author = models.CharField(max_length = 45)
	xmlsitemap = models.BooleanField(default = True)
	xmlsitemap_prioridad = models.CharField(max_length = 4)

	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)

	def __unicode__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		super(Movie, self).save(*args, **kwargs)


class Post(models.Model):

	category = models.ManyToManyField(Category)
	tag = models.ManyToManyField(Tag)
	user = models.ForeignKey(User)

	title = models.CharField(max_length = 50)
	slug = models.SlugField(max_length = 50)
	title_hidden = models.BooleanField(default = True)
	description_short = RichTextField()
	description_large = RichTextField()
	description_extra = models.TextField()
	multimedia_imagen_destacado = models.ImageField(upload_to = 'posts')
	status = models.BooleanField(default = True)
	orden = models.IntegerField()
	meta_title = models.CharField(max_length = 50)
	meta_description = models.TextField()
	meta_keywords = models.CharField(max_length = 250)
	meta_author = models.CharField(max_length = 45)
	xmlsitemap = models.BooleanField(default = True)
	xmlsitemap_prioridad = models.CharField(max_length = 4)
	status_comment = models.BooleanField(default = True)

	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)

	def __unicode__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		super(Movie, self).save(*args, **kwargs)

class Comment(models.Model):

	user = models.ForeignKey(User, null = True, blank = True)
	post = models.ForeignKey(Post)
	title = models.CharField(max_length = 50)
	slug = models.SlugField(max_length = 50)
	description = models.TextField()
	status = models.BooleanField(default = True)
	name = models.CharField(max_length = 255)
	email = models.EmailField()
	web = models.CharField(max_length = 100)

	def __unicode__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		super(Movie, self).save(*args, **kwargs)