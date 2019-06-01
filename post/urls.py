from django.contrib import admin
from django.urls import path,include
from .import views


app_name="post_app"


urlpatterns = [
    path('newsfeed/',views.index,name="index"),
    path('',views.main,name="main"),


    # path('post/<int:pk>',views.index,name="index"),


    path('edit/<int:pk>',views.update,name="update"),
    path('delete/<int:pk>',views.delete,name="delete"),
    path('<int:pk>/',views.details,name="details"),
    path('like/',views.like,name="post-like"),
    path('posts/',views.all_post,name="allposts"),


    

]
