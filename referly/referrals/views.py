from django.views.generic.edit import UpdateView
from django.views.generic import ListView, TemplateView
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy as reverse

from .models import Referral
from .forms import ReferralUpdateForm
from utils import get_object_or_none, SetupViewMixin

from braces.views import LoginRequiredMixin

class ReferralListView(LoginRequiredMixin, ListView):
    """
    View for list of referrals for current user.
    """
    template_name = 'referrals/referral_list.html'
    context_object_name = 'referral_list'

    def get_queryset(self):
        return self.request.user.referrals.all()


class ReferralUpdateView(LoginRequiredMixin, UpdateView):
    """
    View to update particulr referral details.
    """
    model = Referral
    slug_field = 'slug'
    slug_url_kwarg = 'referral_id'
    form_class = ReferralUpdateForm
    template_name = 'referrals/referral_update.html'
    success_url = reverse('referrals:referral_list')


class LandingView(SetupViewMixin, TemplateView):
    """
    View for generic landing page. If query parameter includes a referral code, referral click
    count is increased by one.
    """
    template_name = 'referrals/generic_landing_page.html'

    def setup(self, *args, **kwargs):
        super(LandingView, self).setup(*args, **kwargs)
        self.referral_id = self.request.GET.get('link')
        self.referral_object = get_object_or_none(Referral, slug=self.referral_id)

    def get(self, *args, **kwargs):
        """
        If query parameter is correct, increase the referral click
        """
        if self.referral_object:
            self.referral_object.clicks += 1
            self.referral_object.save()
        return super(LandingView, self).get(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(LandingView, self).get_context_data(*args, **kwargs)
        context['referral_id'] = self.referral_object
        return context