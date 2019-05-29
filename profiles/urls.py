from django.contrib import admin
from django.urls import path,include
from .import views


app_name="profilies"


urlpatterns = [  
    # path('profile/',views.profile,name="profile-form"),
    path('profile-edit/',views.profile_update,name="profile-update"),
    path('<str:username>/follow/',views.Userfollow,name="follow"),
    path('',views.search,name="search"),
    path('<str:author>/',views.profile,name="profile"),
    path('<str:author>/photos',views.profile_p,name="photos"),
    path('<str:author>/about',views.profile_a,name="about"),
    path('user/followers/',views.follow_list,name="followers"),

]
