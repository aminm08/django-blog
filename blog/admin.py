from django.contrib import admin
from .models import BlogPost
@admin.register(BlogPost)
class Settings(admin.ModelAdmin):
    list_display = ['title','status','author','datetime_created']

