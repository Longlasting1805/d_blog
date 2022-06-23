from django.contrib import admin

# Register your models here.
from .models import blog_model

admin.site.register(blog_model)
