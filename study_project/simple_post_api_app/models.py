from django.contrib.auth.models import User
from django.db import models

from django.utils.translation import gettext as _

# Create your models here.
class SimplePost(models.Model):

    # The id field will be auto-created

    header = models.CharField(max_length=200, blank=False, null=False, verbose_name=_("Header"))
    content = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=200, blank=True, null=True)
