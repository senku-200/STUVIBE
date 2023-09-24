from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.db.models import Max
from . import choices 
from ckeditor_uploader.fields import RichTextUploadingField
class User(AbstractUser):
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    dob = models.DateField(null=True,blank=True)#
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
    followers = models.ManyToManyField('self',blank=True)
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
    class Meta:
        ordering = ['-updated','-created']
    def __str__(self):
        return self.title
    
class Post(models.Model):
    post_details = models.ForeignKey(PostDetails,on_delete=models.CASCADE,related_name='post_details')
    post = models.FileField(upload_to='./static/data/posts')
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-updated','-created']
    

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(PostDetails,on_delete=models.CASCADE,related_name='comments')
    content = models.TextField()
    likes = models.ManyToManyField(User,related_name='liked_comment',blank=True)
    parent_comment = models.ForeignKey('self',on_delete=models.CASCADE,related_name='replies',null=True,blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-updated','-created']
    def __str__(self):
        return self.content

    

class Stories(models.Model):
    host = models.ForeignKey(User,on_delete=models.CASCADE)
    story = models.FileField(upload_to='./static/data/stories')
    tags = models.TextField(blank=True,null=True)
    likes = models.ManyToManyField(User,related_name='liked_Story',blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
 
    

    
LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

class Like(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostDetails, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, max_length=8)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    

job_type_choices = [
    ('freelancer','freelancer'),
    ('job','job')
]
flexibility_choices = [
    ('fulltime','fulltime'),
    ('parttime','parttime')
]
class Portfolio(models.Model):
    portfolio_user = models.ForeignKey(User,on_delete=models.CASCADE)
    portfolio_username = models.CharField(max_length=500,default='')
    followers = models.ManyToManyField(User,related_name='portfolio_followers',blank=True)
    job_type = models.TextField(choices=job_type_choices)
    flexibility = models.TextField(choices=flexibility_choices)
    domain = models.TextField(blank=True,null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.portfolio_username

class PortfolioProjectsDetails(models.Model):
    portfolio = models.ForeignKey(Portfolio,related_name='portfolio',on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    description = models.TextField(blank=True,null=True)
    tags = models.TextField(blank=True,null=True)
    tools_used = models.TextField(blank=True,null=True)
    project_cover = models.ImageField(upload_to='./static/data/project_cover',null=True,blank=True)
    appreciations = models.ManyToManyField(User,related_name='appreciations',blank=True)
    views = models.ManyToManyField(User,related_name='portfolio_views',blank=True)
    project_files = RichTextUploadingField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title



class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    reciepient = models.ForeignKey(User,on_delete=models.CASCADE,related_name='to_user')
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name='from_user')
    is_read = models.BooleanField(default=False)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def sender_message(from_user,to_user,body):
        sender_message = Message(
            user = from_user,
            sender = from_user,
            reciepient = to_user,
            body = body,
            is_read = True
        )
        sender_message.save()
        reciepient_message = Message(
            user = to_user,
            sender = from_user,
            reciepient = from_user,
            body = body,
            is_read = True
        )
        reciepient_message.save()

        return sender_message
    def get_message(user):
        users = []
        messages = Message.objects.filter(user = user).values('reciepient').annotate(last=Max('date')).order_by("-last")
        for message in messages:
            users.append({
                'user':User.objects.get(pk=message['reciepient']),
                'last':message['last'],
                'unread':Message.objects.filter(user=user,reciepient__pk = message['reciepient'],is_read = False).count()
            })
        return users

 
 