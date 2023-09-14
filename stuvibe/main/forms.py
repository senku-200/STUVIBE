from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models
from ckeditor.widgets import CKEditorWidget

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
        fields = ['content']
class PortfolioForm(ModelForm):
    class Meta:
        model = models.Portfolio
        fields = ['portfolio_username','job_type','flexibility','domain']
        
class PortfolioProjectsDetailsForm(ModelForm):
    class Meta:
        model = models.PortfolioProjectsDetails
        fields = ['project_files']


 