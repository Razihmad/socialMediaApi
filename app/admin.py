from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['user','followers','followings']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user','title']
    
    
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['post','likes']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post','user','content']
    