from django.contrib import admin
from .models import Category, Tag, Post, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

	list_display = ('id' ,'user', 'title', 'slug', 'created')
	list_editable = ('user',)
	fieldsets = (
			(None, {
				'fields' : ('category', 'tag', 'title', 'slug', 
							'title_hidden', 'description_short', 'description_large',
							'description_extra', 'multimedia_imagen_destacado', 'status',
							'orden', 'meta_title', 'meta_description', 'meta_keywords',
							'meta_author', 'xmlsitemap', 'xmlsitemap_prioridad', 'status_comment')
				}),
		)

	def save_model( self, request, obj, form, change ):
		obj.user = request.user
		obj.save()

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	pass