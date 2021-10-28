from django.urls import path
from django.contrib.auth import views as auth_views

from .views import (
    home, 
    about, 
    login, 
    register, 
    addpost, 
    profile, 
    profileupdate, 
    profileadd,
    like
    )

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    # path('login', login, name='login'),
    path('register', register, name='register'),

    # profile
    path('profile', profile, name='profile'),
    path('profileadd', profileadd, name='profileadd'),
    path('profileupdate', profileupdate, name='profileupdate'),

    # post
    path('addpost', addpost, name='addpost'),

    # auth_views (login, logout)
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

    # actions
    path('like/<int:id>', like, name='like'),
]