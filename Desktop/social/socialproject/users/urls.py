from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('login/', views.user_login, name="login"),
    path('logout/', views.logout_view, name='logout'),
    path('', views.index, name="index"),
]