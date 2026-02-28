from django.contrib import admin
from .models import Note
# Register your models here.
admin.site.register(Note) #registered the Note model with the admin site to allow us to manage notes through the Django admin interface