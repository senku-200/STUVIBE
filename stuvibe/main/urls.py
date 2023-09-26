from django.contrib import admin
from django.urls import path,include
from . import views
# app_name = 'stuvibe'
urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('edit_profile/<str:pk>',views.signup_edit,name='edit_profile'),
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
    path('projects/<str:pk>', views.projects, name="projects"),
    path('search_users', views.search_users, name="search_users"),
    path('search_posts', views.search_posts, name="search_posts"),
    path('display_posts/<str:pk>', views.display_posts, name="display_posts"),
]
    



