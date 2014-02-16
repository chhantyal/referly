from django.contrib.auth import get_user_model

from referrals.models import Referral
from .serializers import UserSerializer, ReferralSerializer

from rest_framework import generics

class UserRetriveAPIView(generics.RetrieveAPIView):
    """
    API endpoint for an user and referrals.
    """
    model = get_user_model()
    serializer_class = UserSerializer
    lookup_field = 'username'


class ReferralListCreateAPIView(generics.ListCreateAPIView):
    """
    API endpoint for referrals.
    """
    model = Referral
    serializer_class = ReferralSerializer

    def pre_save(self, obj):
        obj.user = self.request.user


class ReferralRetreveUpdateAPIView(generics.RetrieveUpdateAPIView):
    """
    API endpoint for retreving and updating a referral. Referral unique id i.e slug should be
    provided.
    """
    model = Referral
    serializer_class = ReferralSerializer
    lookup_field = 'slug'


class ReferralRetriveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for retreving and removing a referral. Referral unique id i.e slug should be
    provided.
    """
    model = Referral
    serializer_class = ReferralSerializer
    lookup_field = 'slug'



