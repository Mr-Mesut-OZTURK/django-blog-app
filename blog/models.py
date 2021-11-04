from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.

# class User(models.Model): # ok
#     name = models.CharField(max_length=50)
#     email = models.EmailField(max_length=200)
#     password = models.CharField(max_length=255)

class Profile(models.Model):  # ok
    image = models.ImageField(upload_to="profiles/%Y", default="default.jpg")
    bg_image_url = models.CharField(
        max_length=254,
        null=True,
        blank=True,
        help_text="Zorunlu değil, Eğer resim kaybolursa arkaplan fotoğrafı olarak bu url adresindeki fotoğraf kalır"
    )
    bio = models.TextField(max_length=5000, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Category(models.Model):  # ok
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):  # ok
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to="posts/%Y")
    bg_image_url = models.CharField(
        max_length=254,
        null=True,
        blank=True,
        help_text="Zorunlu değil, Eğer resim kaybolursa arkaplan fotoğrafı olarak bu url adresindeki fotoğraf kalır"
    )
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = (
        ("active", "active"),
        ("deactive", "deactive"),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    slug = models.SlugField(
        verbose_name='slug',
        allow_unicode=True,
        unique=True,
        max_length=255,
        default=title,
        help_text=(
            "The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/")
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title + " " + self.status


class Comment(models.Model):  # ok
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=2000)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='comments')

    def __str__(self):
        return self.user.username.title() + ' - ' + self.post.title


class PostView(models.Model):  # ok
    timestamp = models.TimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='views')
    posts = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='views')

    def __str__(self):
        return str(self.user) + ' - ' + self.posts.title


class Like(models.Model):  # ok
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="likes")
    posts = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, related_name="likes")

    def __str__(self):
        return self.user.username + ' - ' + self.posts.title

    class Meta:
        # db_table = 'likes'
        constraints = [
            models.UniqueConstraint(
                fields=['posts', 'user'], name="unique_like")
        ]
        # unique_together = ('user', 'posts',)
