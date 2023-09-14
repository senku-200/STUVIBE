from django.contrib import admin
from django.urls import path,include
from . import views
# app_name = 'stuvibe'
urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('createpost',views.create_post,name='create_post'),
    path('login',views.login_,name='login'),
    path('profile/<int:pk>',views.profile,name='profile'),
    path('liked/', views.like_unlike_post, name='like-post-view'),
    path('comments/<int:pk>', views.comments, name='comments'),
    path('create_portfolio', views.create_portfolio, name='create_portfolio'),
    path('createproject', views.createproject, name='createproject'),
    path('portfoliohome', views.PortfolioHome, name='PortfolioHome'),
    path('inbox/', views.inbox, name='inbox'),
    path('direct/<username>', views.Directs, name="directs"),
    path('send/', views.SendDirect, name="send-directs"),
    path('search/', views.UserSearch, name="search-users"),
    path('new/<username>', views.NewConversation, name="conversation"),
    path('direct/getMessages/<str:username>/', views.getMessages, name="getMessages"),
    path('portfolio', views.PortfolioHome, name="portfolio"),
]
    



