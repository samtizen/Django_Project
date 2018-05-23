from django.db import models


# Create your models here.
class SimplePost(models.Model):

    # The id field will be auto-created

    header = models.CharField(max_length=200, blank=False, null=False)
    content = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("testapp_simple-post-list", kwargs={"pk": self.id})