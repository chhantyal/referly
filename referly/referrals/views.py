from django.views.generic.edit import UpdateView
from django.views.generic import ListView, TemplateView
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy as reverse

from .models import Referral
from .forms import ReferralUpdateForm

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