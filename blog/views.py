from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

from .models import (
    Profile,
    Post,
    Like,
    Comment,
    PostView,
)

from .forms import (
    PostForm,
    ProfileForm,
    RegisterForm,
    LikeForm,
    CommentForm
)

from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.views import View


# Create your views here.
def home(request):  # ok

    posts = Post.objects.filter(status='active')
    likeform = LikeForm()

    if request.method == 'POST':
        if 'like' in request.POST:
            if request.user.is_authenticated:
                # print('Like request', request.POST)
                user = User.objects.get(id=request.user.id)
                post = Post.objects.get(slug=request.POST['slug'])
                # print(post)
                b1 = Like(user=user, posts=post)
                instance = Like.objects.filter(user=b1.user, posts=b1.posts)
                if instance:
                    instance.delete()
                    # likeform = LikeForm()
                    return redirect('home')
                else:
                    b1.save()
                    # likeform = LikeForm()
                    return redirect('home')
            else:
                return redirect('login')


    context = {
        'posts': posts,
        'likeform': likeform,
    }
    return render(request, 'home.html', context)


def about(request):  # ok
    return render(request, 'about.html')


def register(request):  # ok

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Your account has been created. You can log in now!')
            return redirect('login')
    else:
        form = RegisterForm()

    context = {'form': form}
    return render(request, 'register.html', context)


def profile(request):  # ok

    if not request.user.is_authenticated:
        return redirect('login')

    posts = Post.objects.filter(user=request.user.id)
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None

    context = {
        'posts': posts,
        'profile': profile,
    }

    return render(request, 'profile.html', context)


def profileadd(request):  # ok

    if not request.user.is_authenticated:
        return redirect('login')

    form = ProfileForm()

    if request.method == 'POST':
        user = User.objects.get(pk=request.user.id)

        form = ProfileForm(request.POST, request.FILES, instance=user)

        # id otomatik olarak buradan yüklenir
        # Return an object without saving to the DB
        # obj = form.save(commit=False)
        # obj.user = User.objects.get(pk=request.user.id)

        if form.is_valid():

            form.save()
            messages.success(
                request, f'Your account has been created. You can log in now!')
            return redirect('profile')

    context = {
        'form': form,
    }

    return render(request, 'profileadd.html', context)


def profileupdate(request):  # ok
    if not request.user.is_authenticated:
        return redirect('login')

    user = Profile.objects.get(user=request.user.id)
    form = ProfileForm(instance=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            form.save()
            messages.success(
                request, f'Your account has been created. You can log in now!')
            return redirect('profile')

    context = {
        'form': form,
    }
    return render(request, 'profileupdate.html', context)


def addpost(request):  # ok
    if not request.user.is_authenticated:
        return redirect('login')

    form = PostForm()

    if(request.method == 'POST'):
        form = PostForm(request.POST, request.FILES)

        # id otomatik olarak buradan yüklenir
        # Return an object without saving to the DB
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=request.user.id)

        if(form.is_valid()):
            form.save()
            return redirect('profile')

    context = {
        'form': form,
    }
    return render(request, 'addpost.html', context)


def updatepost(request, id):  # ok
    if not request.user.is_authenticated:
        return redirect('login')

    post = Post.objects.get(pk=id)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return redirect('profile')

    context = {
        'form': form,
    }

    return render(request, 'updatepost.html', context)


def deletepost(request, id):  # ok
    if not request.user.is_authenticated:
        return redirect('login')

    post = Post.objects.get(pk=id)
    form = PostForm(instance=post)

    if request.method == 'POST':
        post.delete()
        return redirect('profile')

    context = {
        'form': form,
    }

    return render(request, 'deletepost.html', context)


def postdetail(request, slug):
        
    post = Post.objects.get(slug=slug)
    comments = Comment.objects.filter(post=post.id)
    commentform = CommentForm()
    likeform = LikeForm()

    # Post view increment
    if not 'like' in request.POST:
        if not 'comment' in request.POST:
            if request.user.is_authenticated:
                user = User.objects.get(pk=request.user.id)
                postview = PostView(posts=post, user=user)
                postview.save()
            else:
                postview= PostView(posts=post)
                postview.save()


    if request.method == 'POST':
        # if not authenticate dont show another codes
        if not request.user.is_authenticated:
            return redirect('login')

        # Like request
        if 'like' in request.POST:
            print('Like request')
            user = User.objects.get(id=request.user.id)
            post = Post.objects.get(slug=slug)
            b1 = Like(user=user, posts=post)
            instance = Like.objects.filter(user=b1.user, posts=b1.posts)
            if instance:
                instance.delete()
            else:
                b1.save()
        # comment request
        elif 'comment' in request.POST:
            print('comment request')
            form = CommentForm(request.POST)

            # Return an object without saving to the DB
            obj = form.save(commit=False)
            obj.user = User.objects.get(pk=request.user.id)
            obj.post = Post.objects.get(slug=slug)

            if form.is_valid():
                form.save()
                form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'commentform': commentform,
        'likeform': likeform,
    }

    return render(request, 'postdetail.html', context)
