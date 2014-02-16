# -*- coding: utf-8 -*-
from django import forms

from .models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User

        # Constrain the UserForm to just these fields.
        fields = ("first_name", "last_name")