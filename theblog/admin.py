from django.contrib import admin
from .models import Post, Comment, Critique, Profile
# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Critique)
admin.site.register(Profile)
