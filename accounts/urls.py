from django.contrib import admin
from django.urls import path,include
from .import views
from django.contrib.auth import views as auth_views

app_name="accounts"


urlpatterns = [
    
    path('signup/',views.signup,name='signup'),
    path('account-settings/',views.account_settings,name='account-setting'),
    path('password/',views.passchange,name='passchange'),
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name='accounts/login.html'),name="logout"),

]