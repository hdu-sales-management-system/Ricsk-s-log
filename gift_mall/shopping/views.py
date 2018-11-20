from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.http import JsonResponse
import json
# Create your views here.
from .models import *


#done
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
            request.session['USER_Id'] = user[0].id
            conx = serializers.serialize("json", user)
            conx2 = '{"log_status": 1, "user": ' + conx + '}'
            return HttpResponse(conx2,content_type="application/json")
        else:
            return HttpResponse(json.dumps(context),content_type="application/json")


#done
def logout(request):
    context={
        'IS_LOGOUT': 0
    }
    if('IS_LOGIN' in request.session and 'USER_Id' in request.session):
        del request.session['IS_LOGIN']
        del request.session['USER_Id']
        context['IS_LOGOUT'] = 1
        return HttpResponse(json.dumps(context), content_type="application/json")
    else:
        return HttpResponse(json.dumps(context), content_type="application/json")


#done
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


#done
def tags(request):
    tags = Tag.objects.all()
    conx = serializers.serialize("json", tags)
    return HttpResponse(conx, content_type="application/json")

#done
def categorise(request):
    if request.method == 'GET':
        category = Category.objects.all()
        conx = serializers.serialize("json", category)
        return HttpResponse(conx, content_type="application/json")
    if request.method == 'POST':
        id = request.POST.get('id')
        category = Category.objects.filter(categoryP=id)
        conx = serializers.serialize("json", category)
        return HttpResponse(conx, content_type="application/json")


#done
def carousel(request):
    carousel = Crousel.objects.all()
    conx = serializers.serialize("json", carousel)
    return HttpResponse(conx, content_type="application/json")


#done
def gifts_son(request, present_id):
    context = {
        'gift_status': 0
    }
    if request.method == 'GET':
        gifts_son = Present.objects.filter(pk=present_id)
        if(gifts_son):
            if(gifts_son[0].status == 1):
                conx = serializers.serialize("json", gifts_son)
                conx2 = '{"gift_status": 1, "gift": ' + conx + '}'
                return HttpResponse(conx2, content_type="application/json")
            else:
                return HttpResponse(json.dumps(context), content_type="application/json")
        else:
            return HttpResponse(json.dumps(context), content_type="application/json")


def car(request, user_id):
    user = User.objects.get(pk=user_id)
    context = {
        'error': 0
    }
    if (not user) or ('USER_Id' not in request.session) or ('IS_LOGIN' not in request.session) \
            or (request.session['USER_Id'] != user_id):
        context['error'] = 1
        return HttpResponse(json.dumps(context), content_type="application/json")
    if request.method == 'GET':
        present = User.objects.filter(pk=user_id)[0].car_set.all()
        cart = []
        for p in present:
            cart.append(p.present)
        conx = serializers.serialize("json", cart)
        return HttpResponse(conx, content_type="application/json")
    if request.method == 'POST':
        return
    if request.method == 'DELETE':
        return
    if request.method == 'PUT':
        return




#需要讨论
def orders(request, user_id):
    return

def buy(request, order_id):
    return
#需要讨论
def search(request):
    return
