from __future__ import unicode_literals
import uuid

from django.db import models, IntegrityError
from django.utils.text import slugify
from django.utils import timezone


class Referral(models.Model):
    """
    Main models for referrals app.
    """
    title = models.CharField(max_length=250)
    slug = models.CharField(unique=True, blank=True, max_length=250)
    user = models.ForeignKey('users.User', related_name='referrals')
    date_created = models.DateTimeField(auto_now_add=True, default=timezone.now())
    date_updated = models.DateTimeField(auto_now=True, default=timezone.now())
    is_active = models.BooleanField(default=True)
    clicks = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        When slug/referral_id is not given, slugfy title, make it unique and save it as slug
        """
        if not self.slug:
            # make it unique using uuid module
            self.slug = slugify("{slug}-{uid}".format(slug=self.title,
                                                    uid=unicode(uuid.uuid4())[:4]))
        super(Referral, self).save(*args, **kwargs)