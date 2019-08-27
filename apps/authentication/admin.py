from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.authentication.models import User

from .models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'username', 'password']


admin.site.register(User, CustomUserAdmin)
