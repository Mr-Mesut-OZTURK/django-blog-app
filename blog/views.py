from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')