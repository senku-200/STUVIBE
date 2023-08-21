from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

from . import choices 
class User(AbstractUser):
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    dob = models.DateField(null=True,blank=True)
    profile_photo = models.ImageField(upload_to='./static/data/user_profile',blank=True,null=True)
    profile_banner = models.ImageField(upload_to='./static/data/profile_banner',blank=True,null=True)
    degree = models.TextField(null=True,blank=True)
    branch = models.TextField(null=True,blank=True)
    country = models.TextField(null=True,blank=True)
    state = models.TextField(max_length=100,null=True,blank=True)
    district = models.TextField(max_length=100,null=True,blank=True)
    bio = models.TextField(null=True,blank=True)
    university = models.TextField(null=True,blank=True)
    aspiring = models.TextField(null=True,blank=True)
    gender = models.TextField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.username
    
class PostDetails(models.Model):
    host = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    template = models.ImageField(upload_to='./static/data/post_templates',null=True,blank=True)
    content = models.TextField(blank=True,null=True)
    tags = models.TextField(blank=True,null=True)
    likes = models.ManyToManyField(User,related_name='liked_post',blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
class Post(models.Model):
    post_details = models.ForeignKey(PostDetails,on_delete=models.CASCADE,related_name='post_details')
    post = models.FileField(upload_to='./static/data/posts')
    

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    content = models.TextField()
    likes = models.ManyToManyField(User,related_name='liked_comment',blank=True)
    parent_comment = models.ForeignKey('self',on_delete=models.CASCADE,related_name='replies',null=True,blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.content

    


    

    