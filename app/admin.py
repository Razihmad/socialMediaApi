from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['user','followers','followings']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user','title']
    