from django.contrib import admin

# Register your models here.
from .models import SimplePost

admin.site.register(SimplePost)