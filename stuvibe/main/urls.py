from django.contrib import admin
from django.urls import path
from . import views
# app_name = 'stuvibe'
urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('createpost',views.create_post,name='create_post'),
    path('login',views.login_,name='login'),
    path('profile',views.profile,name='profile'),
    path('liked/', views.like_unlike_post, name='like-post-view'),
    path('comments/<int:pk>', views.comments, name='comments'),
]