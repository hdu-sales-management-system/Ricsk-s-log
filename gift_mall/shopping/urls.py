
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('/login', views.login, name='login'),
    path('/logout', views.logout, name='logout'),
    path('/register', view.register, name='register'),
    path('/gifts', view.gifts, name='gifts'),
    path('/tags', view.tags, name='tags'),
    path('/cateogries', view.cateogries, name='cateogries'),
    path('/carouse', view.carouse, name='carouse'),

]