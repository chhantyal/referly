from django.conf.urls import patterns, include, url

from .views import ReferralListView, ReferralUpdateView


urlpatterns = patterns('',

    url(r'^$', ReferralListView.as_view(), name='referral_list'),
    url(r'(?P<referral_id>[\w-]+)/$', ReferralUpdateView.as_view(), name='referral_update'),
)
