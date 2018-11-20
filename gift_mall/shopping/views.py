from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.http import JsonResponse
import json
# Create your views here.
from .models import *

def login(request):
    context = {
        'log_status': 0
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        print(name,password)
        user = User.objects.filter(name = name, password = password)
        if user:
            request.session['IS_LOGIN'] = True
            conx = serializers.serialize("json", user)
            conx2 = '{"log_status": 1, "user": ' + conx + '}'
            return HttpResponse(conx2,content_type="application/json")
        else:
            return HttpResponse(json.dumps(context),content_type="application/json")


def logout(request):
    context={
        'IS_LOGOUT': 0
    }
    if('IS_LOGIN' in request.session):
        del request.session['IS_LOGIN']
        context['IS_LOGOUT'] = 1
        return HttpResponse(json.dumps(context), content_type="application/json")
    else:
        return HttpResponse(json.dumps(context), content_type="application/json")

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        pwd = request.POST.get('password')
        address = request.POST.get('address')
        birthday = request.POST.get('birthday')
        nickname = request.POST.get('nickname')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        user = User.objects.filter(name=name, password=pwd)
        context = {'re_true': 0}
        if name and pwd and not user:
            u = User(name=name,
                     password=pwd,
                     address=address,
                     birthday=birthday,
                     nickname=nickname,
                     gender=gender,
                     phone=phone)
            u.save()
            context['re_true'] = 1
            return HttpResponse(json.dumps(context), content_type="application/json")
        else:
            context['re_true'] = 0
            return HttpResponse(json.dumps(context), content_type="application/json")


def gifts(request):
    return


def tags(request):
    tags = Tag.objects.all()
    conx = serializers.serialize("json", tags)
    return HttpResponse(conx, content_type="application/json")


def categorise(request):
    if request.method == 'GET':

    if reqeust.method == 'POST':

def carousel(request):
    return

def gifts_son(request, present_id):
    return

def car(request, user_id):
    return

def orders(request, user_id):
    return

def buy(request, order_id):
    return

def search(request):
    return
