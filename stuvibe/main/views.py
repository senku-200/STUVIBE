from django.shortcuts import render,redirect
from . import models
# Create your views here.
from . import forms
from django.contrib.auth import login,logout 
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def profile(request,pk):
    user = models.User.objects.get(id = pk)
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
            # user.profile_photo = request.POST['profile_photo']
            # user.profile_banner = request.POST['profile_banner']
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
        return redirect('home')
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
            return redirect('home')
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

from django.http import HttpResponse

def create_portfolio(request):
    existing_portfolio = models.Portfolio.objects.filter(portfolio_user=request.user).first()
    if existing_portfolio:
        return redirect('portfolio')
    if request.method == 'POST':
        portfolio = forms.PortfolioForm(request.POST)
        if portfolio.is_valid():
            portfolio = portfolio.save(commit=False)
            portfolio.portfolio_user = request.user
            portfolio.save()
            return redirect('portfolio')
        else:
            print(portfolio.errors)
    form = forms.PortfolioForm()
    context = {
        'form':form,
        'leftsidebar':'lite',
    }
    return render(request,'create_portfolio.html',context=context)
from django.shortcuts import get_object_or_404

def createproject(request):
    portfolio  = models.Portfolio.objects.filter(portfolio_user = request.user).first()
    form = forms.PortfolioProjectsDetailsForm()
    if request.method == 'POST':
        form = forms.PortfolioProjectsDetailsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.portfolio = portfolio
            form.title = request.POST.get('title')
            form.description = request.POST.get('description')
            form.tags = request.POST.get('tags')
            form.tools_used = request.POST.get('tools_used')
            form.project_cover = request.FILES.get('project_cover')
            form.save()
        else:
            print(form.errors)
    context = {'form':form,'leftsidebar':'lite','user':request.user}
    return render(request,'createproject.html',context)


def PortfolioHome(request):
    portfolios = models.Portfolio.objects.all()
    context = {
        'portfolios':portfolios,
        'leftbar':'lite'
    }
    return render(request,'PortfolioHome.html',context)




from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Message
from .models import User
from django.db.models import Q
from django.core.paginator import Paginator

@login_required
def inbox(request):
    user = request.user
    messages = Message.get_message(user=request.user)
    active_direct = None
    directs = None
    # profile = get_object_or_404(User, user=user)
    if messages:
        message = messages[0]
        active_direct = message['user']
        directs = Message.objects.filter(user=request.user, reciepient=message['user'])
        directs.update(is_read=True)
        for message in messages:
            if message['user'].username == active_direct:
                message['unread'] = 0
    context = {
        'directs':directs,
        'messages': messages,
        'active_direct': active_direct,
        # 'profile': profile,
        'leftsidebar':'lite',
        'display':False,
    }
    return render(request, 'directs/direct.html', context)

@login_required
def Directs(request, username):
    
    user  = request.user
    messages = Message.get_message(user=user)
    active_direct = models.User.objects.get(username = username)
    directs = Message.objects.filter(user=user, reciepient__username=username)  
    directs.update(is_read=True)
    if request.method == "POST":
        body = request.POST.get('body')
        to_user = User.objects.get(username=username)
        Message.sender_message(user, to_user, body)
    for message in messages:
            if message['user'].username == username:
                message['unread'] = 0
    context = {
        'directs': directs,
        'messages': messages,
        'active_direct': active_direct,
        'leftsidebar':'lite',
        'display':True,
    }
    return render(request, 'directs/direct.html', context)

def SendDirect(request):
    from_user = request.user
    to_user_username = request.POST.get('to_user')
    body = request.POST.get('body')

    if request.method == "POST":
        to_user = User.objects.get(username=to_user_username)
        Message.sender_message(from_user, to_user, body)
        return redirect('directs')

def UserSearch(request):
    query = request.GET.get('q')
    context = {}
    if query:
        users = User.objects.filter(Q(username__icontains=query))

        # Paginator
        paginator = Paginator(users, 8)
        page_number = request.GET.get('page')
        users_paginator = paginator.get_page(page_number)

        context = {
            'users': users_paginator,
            }

    return render(request, 'directs/search.html', context)

def NewConversation(request, username):
    from_user = request.user
    body = ''
    try:
        to_user = User.objects.get(username=username)
    except Exception as e:
        return redirect('search-users')
    if from_user != to_user:
        Message.sender_message(from_user, to_user, body)
    return redirect('message')


from django.http import JsonResponse
def getMessages(request,username):
    user = request.user
    directs = Message.objects.filter(user=user, reciepient__username=username)  
    return JsonResponse({"messages":list(directs.values())})