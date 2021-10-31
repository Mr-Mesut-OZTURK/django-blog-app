from django.forms import ModelForm
from .models import Profile, Post, Comment, PostView, Like
from django.contrib.auth.models import User 

from django.contrib.auth.forms import UserCreationForm

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',
            'bg_image_url',
            'status',
            'slug',
            'category',
        ]

class ProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = ['image', 'bg_image_url', 'bio']

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class LikeForm(ModelForm):

    class Meta:
        model = Like
        fields = [
            # 'user', 
            # 'posts'
            ]

class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['content']