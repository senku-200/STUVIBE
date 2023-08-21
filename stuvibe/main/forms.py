from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models
class UserForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = ['username','email','first_name','last_name','dob','profile_photo','profile_banner','degree','branch','country','state','district','bio','university','gender']
        
class CreatePost(ModelForm):
    class Meta:
        model = models.PostDetails
        fields = ['title','content','tags']
        
        
        
class CreateComment(ModelForm):
    class Meta:
        model = models.Comment
        fields = ['post','content']
        widgets = {
            'post': forms.ClearableFileInput(attrs={'multiple': True}),
        }   
        