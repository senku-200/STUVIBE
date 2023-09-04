from django.shortcuts import render,redirect
from . import models
# Create your views here.
from . import forms
from django.contrib.auth import login,logout 
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def profile(request):
    user = models.User.objects.get(id = request.user.id)
    post = models.Post.objects.filter(post_details__host = user)
    details = models.PostDetails.objects.filter(host = user)
    context = {
        'user':user,
        'leftsidebar':'lite',
        'post':post,
        'details':details,
    }
    return render(request,'profile.html',context)

@login_required(login_url='login')
def home(request):
    
    post = models.Post.objects.all()
    comments = models.Comment.objects.all()
    stories = models.Stories.objects.all()
    context = {
        'leftsidebar':'',
        'stories':stories,
        'posts':post,
        'comments':comments,
    }
    
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = models.Post.objects.get(id=post_id)
        profile = models.User.objects.get(id = request.user.id)
        if profile in post_obj.post_details.likes.all():
            post_obj.post_details.likes.remove(profile)
        else:
            post_obj.post_details.likes.add(profile)

        like, created = models.Like.objects.get_or_create(user=profile, post_id=post_id)

        if not created:
            if like.value=='Like':
                like.value='Unlike'
            else:
                like.value='Like'
        else:
            like.value='Like'
            post_obj.save()
            like.save()
    
    return render(request,"home.html",context)


def signup(request):
    form = forms.UserForm()
    if request.method == 'POST':
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


@login_required(login_url='login')
def create_post(request):
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
            return redirect('home')
        else:
            print(form.errors)
    context = {'form':form , 'leftsidebar':'lite'}
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

@login_required
def like_unlike_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = models.Post.objects.get(id=post_id)
        profile = models.User.objects.get(user=user)

        if profile in post_obj.post_details.likes.all():
            post_obj.post_details.likes.remove(profile)
        else:
            post_obj.post_details.likes.add(profile)

        like, created = models.Like.objects.get_or_create(user=profile, post_id=post_id)

        if not created:
            if like.value=='Like':
                like.value='Unlike'
            else:
                like.value='Like'
        else:
            like.value='Like'

            post_obj.save()
            like.save()
    return redirect('home')

def comments(request,pk):
    posts = models.Post.objects.get(id = pk)
    postdetails = posts.post_details
    post_comments = models.Comment.objects.filter(post=postdetails)
    if request.method == 'POST':
        print(request.POST)
        comment = forms.CreateComment(request.POST)
        if comment.is_valid():
            comment = comment.save(commit=False)
            comment.post = postdetails
            comment.content = request.POST.get('content')
            comment.user = request.user
            comment.save()
        else:
            print(comment.errors)

    context = {
        'post':posts,
        'comments':post_comments,
        "post_details":postdetails
    }
    return render(request,'comment.html',context)