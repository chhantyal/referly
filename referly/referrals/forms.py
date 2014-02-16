from django import forms

from .models import Referral


class ReferralUpdateForm(forms.ModelForm):

    class Meta:
        model = Referral
        fields=('title', 'slug',)