from django.urls import path
from .views import home, about, login, register

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    # path('login', login, name='login'),
    path('register', register, name='register'),
]