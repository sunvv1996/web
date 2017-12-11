# -*-coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class BBS(models.Model):
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=256,blank=True, null=True)
    content = models.TextField()
    author = models.ForeignKey('BBS_user')
    view_count = models.IntegerField()
    ranking = models.IntegerField()
    created_at = models.DateTimeField()
    update_at = models.DateTimeField()

    def __str__(self):
        return self.title

# class Comments(models.Model):
#     pass

class Category(models.Model):
    name = models.CharField(max_length=32,unique=True)
    administrator = models.ForeignKey('BBS_user')

class BBS_user(models.Model):
    user = models.OneToOneField(User)
    signature = models.CharField(max_length=128, default='this guy is too lazy to levave anything here')
    photo = models.ImageField(upload_to='upload_imgs/', default="upload_imgs/user-1.jpg")
    def __str__(self):
        return self.user.username
