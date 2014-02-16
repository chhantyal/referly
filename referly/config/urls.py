# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from referrals.views import LandingView, ReferralListView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', ReferralListView.as_view(), name="dashboard"),

    url(r'^about/$',
        TemplateView.as_view(template_name='pages/about.html'), name="about"),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # User management
    url(r'^users/', include("users.urls", namespace="users")),
    url(r'^accounts/', include('allauth.urls')),

    # Uncomment the next line to enable avatars
    url(r'^avatar/', include('avatar.urls')),

    # referrals app
    url(r'^referrals/', include("referrals.urls", namespace="referrals")),

    # API
    url(r'^apiv1/', include("apiv1.urls", namespace="apiv1")),

    # landing page
    url(r'^landing/$', LandingView.as_view(), name="landing"),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
