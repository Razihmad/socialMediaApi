from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class UserInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="user")
    followers = models.IntegerField(default=0)
    followings = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user.username
    
    
class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="postBy")
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=100000)
    createdTime = models.DateTimeField(default=datetime.now())
    
    def __str__(self):
        return self.user.username
        

class Like(models.Model):
    post = models.OneToOneField(Post,on_delete=models.CASCADE,related_name="post")
    likes = models.IntegerField(default=0) 

    
