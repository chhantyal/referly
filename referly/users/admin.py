# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class UserAdmin(admin.ModelAdmin):
    create_form_class = UserCreationForm
    update_form_class = UserChangeForm

    list_display = ('username', 'email', 'is_staff',)
    list_filter = ('email',)
    search_fields = ('username', 'email',)

admin.site.register(User, UserAdmin)