from django.urls import path, include
# from IDGenie.views import index, blog
from .import views

app_name ="IDGenie"

urlpatterns = [
    
    # HomePage URL  
    path('', views.index, name='index'),
    
    
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'), # BLog detail View
    
    #Blog Post URL
    path('blog/', views.blogpost, name='blog_list'), # BLog List View
    
    
    # path('create/', views.create_blog_post, name='create_blog_post'), # Blog create view  
    
    path("api/user/avatar/", views.get_user_avatar, name="get_user_avatar"),
  
    
    
]
