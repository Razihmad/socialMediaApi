from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="user")
    followers = models.IntegerField(default=0)
    followings = models.IntegerField(default=0)


# class Post(models.Model):
    # user = models.ForeignKey(User,)