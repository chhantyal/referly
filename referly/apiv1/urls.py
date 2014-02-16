from django.conf.urls import patterns, include, url

from .views import (UserRetriveAPIView, ReferralListCreateAPIView,
                                    ReferralRetriveUpdateDestroyAPIView)

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = patterns('',
    # authentication
    url(r'^token/$', obtain_auth_token),

    # user API endpoint
    url(r'^user/(?P<username>[\w-]+)/$', UserRetriveAPIView.as_view(), name='api_user'),

    # referrals API endpoint
    url(r'^referrals/$', ReferralListCreateAPIView.as_view(), name='api_referrals_list'),

    # referral detail API endpoint
    url(r'^referral/(?P<slug>[\w-]+)/$', ReferralRetriveUpdateDestroyAPIView.as_view(),
                                                name='api_referral_detail'),
)
