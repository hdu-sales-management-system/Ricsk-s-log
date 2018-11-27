from django.db import models
import datetime
from django.utils import timezone
# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    birthday = models.DateTimeField()
    nickname = models.CharField(max_length=200)
    gender = models.IntegerField()
    phone = models.CharField(max_length=200)


class Present(models.Model):
    name = models.CharField(max_length=200)
    on_date = models.DateTimeField()
    store_num = models.IntegerField()
    status = models.IntegerField(default=0)#0代表审核，1代表上架，2代表未上架
    cost = models.DecimalField(max_digits=11, decimal_places=2)
    hot = models.IntegerField(default=0)
    off = models.IntegerField(default=0)#0代表不打折，1代表打折
    off_cost = models.DecimalField(max_digits=3, decimal_places=2,null=True)
    url = models.CharField(max_length=200,null=True)


class Order(models.Model):
    status = models.CharField(max_length=200)
    receive_mark = models.IntegerField(default=0)#0代表未收货，1代表已收货
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    logistics = models.CharField(max_length=200)
    begin_date = models.DateTimeField()
    sum_money = models.DecimalField(max_digits=20, decimal_places=2)
    user_feedback = models.CharField(max_length=200)
    type = models.IntegerField()#0代表是用户的，1代表是供货商的


class OrderItemU(models.Model):
    count = models.IntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    present = models.ForeignKey(Present, on_delete=models.CASCADE)


class Tag(models.Model):
    name = models.CharField(max_length=200)
    hot = models.IntegerField(default=0)


class Category(models.Model):
    name = models.CharField(max_length=200)
    hot = models.IntegerField(default=0)
    categoryP = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)


class Ret(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    present = models.ForeignKey(Present, on_delete=models.CASCADE)


class Rec(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    present = models.ForeignKey(Present, on_delete=models.CASCADE)

class Crousel(models.Model):
    url = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    index = models.IntegerField()

class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    present = models.ForeignKey(Present, on_delete=models.CASCADE)
    number = models.IntegerField(default=1)
