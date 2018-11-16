from django.db import models
import datetime
from django.utils import timezone
# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    order = models.IntergerField()
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
    ondate = models.DateTimeField()
    storenum = models.IntergerField()
    status = models.IntergerField()
    cost = models.DecimalField()
    hot = models.IntergerField()
    off = models.IntergerField()
    offcost = models.DecimalField()

class Order(models.Model):
