# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Referral


class ReferralAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'user',)
    list_filter = ('date_created',)
    search_fields = ('title',)

admin.site.register(Referral, ReferralAdmin)