from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin', admin.site.urls),
    path('signup',views.signup,name='signup'),
    path('createpost',views.create_post,name='create_post'),
    path('login',views.login_,name='login'),
]