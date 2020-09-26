from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import (
    CustomUserChangeForm,
    CustomUserCreationForm
)

User = get_user_model()

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = ('username', 'name', 'email','is_superuser')
    search_fields = ('name',)