from .views import login_view, register_view
from django.contrib.auth.views import  LogoutView
from django.urls import path

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
