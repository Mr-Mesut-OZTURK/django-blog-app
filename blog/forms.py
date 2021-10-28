from django.forms import ModelForm
from .models import Profile, Category, Post, Comment, PostView, Like
from django.contrib.auth.models import User 

from django import forms

from django.contrib.auth.forms import UserCreationForm



class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',
            'status',
            'slug',
            'category',
        ]

class ProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = ['image', 'bio']


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class LikeForm(ModelForm):

    # def __init__(self,user,posts):
    #     super(LikeForm, self).__init__
    #     user = user
    #     posts = posts

    class Meta:
        model = Like
        fields = ['user', 'posts']