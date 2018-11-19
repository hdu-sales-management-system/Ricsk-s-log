from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

#员工模型
class Emploee(models.Model):
    empname = models.CharField(max_length=200) #员工姓名
    emppassword = models.CharField(max_length=200) #员工密码
    emporder = models.IntegerField(choices=((0,'查看权限'),
                                            (1,'查看和修改权限'),
                                            (2,'增删改查权限')), default=0) #员工权限
    empposit = models.CharField(max_length=200) #员工职位
    empphone = models.CharField(max_length=200) #员工联系电话

class User(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    auth = models.IntegerField(default=0)
    address = models.CharField(max_length=200)
    birthday = models.DateTimeField()
    nickname = models.CharField(max_length=200)
    gender = models.CharField(max_length=200,
                              choices=((1,'男'),
                                       (2, '女'),
                                       (0, '无'),
                                       ), default=0)
    phone = models.CharField(max_length=200)


class Present(models.Model):
    name = models.CharField(max_length=200)
    on_date = models.DateTimeField()
    store_num = models.IntegerField()
    status = models.IntegerField(default=0)#0代表未上架，1代表上架
    cost = models.DecimalField(max_digits=11, decimal_places=2)
    hot = models.IntegerField(default=0)
    off = models.IntegerField(default=0)#0代表不打折，1代表打折
    off_cost = models.DecimalField(max_digits=3, decimal_places=2)


class Order(models.Model):
    status = models.CharField(max_length=200)
    receive_mark = models.IntegerField(default=0)#0代表未收货，1代表已收货
    present = models.ForeignKey(Present, on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    present_num = models.DecimalField(max_digits=9, decimal_places=0)
    logistics = models.CharField(max_length=200)
    begin_date = models.DateTimeField()
    sum_money = models.DecimalField(max_digits=20, decimal_places=2)
    user_feedback = models.CharField(max_length=200)
    type = models.IntegerField()#0代表是用户的，1代表是供货商的


class Tag(models.Model):
    name = models.CharField(max_length=200)
    hot = models.IntegerField(default=0)


class Category(models.Model):
    name = models.CharField(max_length=200)
    hot = models.IntegerField(default=0)
    tag = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)


class RelationshipT(models.Model):
    ref = models.ForeignKey(Tag, on_delete=models.CASCADE)
    present = models.ForeignKey(Present, on_delete=models.CASCADE)


class RelationshipC(models.Model):
    ref = models.ForeignKey(Category, on_delete=models.CASCADE)
    present = models.ForeignKey(Present, on_delete=models.CASCADE)
