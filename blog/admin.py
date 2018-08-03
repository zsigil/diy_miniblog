from django.contrib import admin
from .models import Blog, Comment, Author

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


admin.site.register(Author)
admin.site.register(Blog)
admin.site.register(Comment)
