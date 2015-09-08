from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class UserAdmin(UserAdmin):
	"""
		Administrador del Modelo de Usuarios
	"""
	list_display = ('username', 'email', 'first_name', 'last_name','created' )
	list_filter = ("is_superuser", "groups")
	search_fields = ("email", "username")
	ordering = ("username",)
	filter_horizontal = ("groups", "user_permissions")
	fieldsets = (
		('User', {"fields": ("username", "password")}),
		("Personal info", {"fields": ("first_name","last_name","email")}),
		("Permissions", {"fields": ("is_active",
									"is_staff",
									"is_superuser",
									"groups",
									"user_permissions")}),
	)