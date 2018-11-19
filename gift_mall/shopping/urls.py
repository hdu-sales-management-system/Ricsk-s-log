
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('gifts/', views.gifts, name='gifts'),
    path('tags/', views.tags, name='tags'),
    path('categorise/', views.categorise, name='categorise'),#主分类和子分类
    path('carousel/', views.carousel, name='carousel'),
    path('gifts/<int:present_id>/', views.gifts_son, name='gifts_son'),
    path('user/<int:user_id>/car/', views.car, name='car'),
    path('users/<int:user_id>/orders/', views.orders, name='orders'),
    path('buy/<int:order_id>/', views.buy, name='buy'),
    path('search/', views.search, name='search'),
]