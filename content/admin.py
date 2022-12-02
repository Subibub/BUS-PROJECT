from django.contrib import admin

# Register your models here.
from .models import Feed, Comment

admin.site.register(Feed)
admin.site.register(Comment)