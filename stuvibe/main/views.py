from django.shortcuts import render
from . import models
# Create your views here.
from . import forms
from django.contrib.auth import login,logout 
from django.contrib.auth import authenticate
def signup(request):
    form = forms.UserForm()
    if request.method == 'POST':
        print(request.POST['profile_photo'],request.POST['profile_banner'])
        form = forms.UserForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.profile_photo = request.POST['profile_photo']
            user.profile_banner = request.POST['profile_banner']
            user.is_staff = True
            user.save()
        else:
            print(form.errors)
    context = {'form':form}
    return render(request,'signup.html',context)
def create_post(request):
    print(request.user.profile_photo)
    form = forms.CreatePost()
    if request.method == 'POST':
        form = forms.CreatePost(request.POST,request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            tags = form.cleaned_data['tags']
            host = request.user
            files = request.FILES.getlist('post')
            instance = models.PostDetails.objects.create( title=title,content=content,tags=tags,host=host)
            for uploaded_file in files:
                models.Post.objects.create(post_details= instance,post = uploaded_file)
        else:
            print(form.errors)
    context = {'form':form}
    return render(request,'createpost.html',context)
def login_(request):
    if request.user.is_authenticated:
        print('already logined')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            models.User.objects.get(username=username)
        except:
            print('user Doesnt exist')
        user = authenticate(request,username = username,password=password)
        if user is not None:
            login(request,user)
        else:
            print('password is wrong')
    context = {}
    return render(request,'login.html',context=context)