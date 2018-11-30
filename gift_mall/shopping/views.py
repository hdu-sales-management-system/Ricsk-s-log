from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.http import JsonResponse
import json
from django.http import QueryDict
import urllib
# Create your views here.
from .models import *


#done
def login(request):
    context = {
        'log_status': 0,
        'user_id':-1
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        print(name,password)
        user = User.objects.filter(name = name, password = password)
        if user:
            request.session['IS_LOGIN'] = True
            request.session['USER_Id'] = user[0].id
            context['log_status'] = 1
            context['user_id'] = user[0].id
            return HttpResponse(json.dumps(context), content_type="application/json")
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


#done
def user_info(request, user_id):
    user = User.objects.get(pk=user_id)
    context = {
        'error': 0
    }
    if (not user) or ('USER_Id' not in request.session) or ('IS_LOGIN' not in request.session) \
            or (request.session['USER_Id'] != user_id):
        context['error'] = 1
        return HttpResponse(json.dumps(context), content_type="application/json")
    if request.method == 'GET':
        user = User.objects.filter(pk=user_id)
        conx = serializers.serialize("json", user)
        conx2 = '{"error": 0, "user": ' + conx + '}'
        return HttpResponse(conx2, content_type="application/json")


#done
def gifts(request):
    if request.method == 'GET':
        gifts1 = []
        gifts2 = []
        ls_gifts1 = Tag.objects.all()
        ls_gifts2 = Category.objects.all()
        count = request.GET.get('count')
        if not count:
            count = 10
        offset = request.GET.get('offset')
        if not offset:
            offset = 0
        tags = request.GET.getlist('tags')
        #print((tags))
        if tags:
            tags2 = []
            for tag in tags:
                tags2.append(urllib.parse.unquote(tag))
              #  print(urllib.parse.unquote(tag))
            ls_gifts1 = Tag.objects.filter(name__in=tags2)
        categories = request.GET.getlist('categories')
        if categories:
            categories2 = []
            for tag in categories:
                categories2.append(urllib.parse.unquote(tag))
            ls_gifts2 = Category.objects.filter(name__in=categories2)
        #print(ls_gifts1)
        #print(ls_gifts2)
        for ls_gifts1_l in ls_gifts1:
            #print(ls_gifts1_l.name)
           # print(3)
            try:
                s = ls_gifts1_l.ret_set.all()
                #print(2)
                for ls in s:
                    ss = ls.present
                    gifts1.append(ss)
            except:
                pass
        for ls_gifts2_l in ls_gifts2:
            try:
                s = ls_gifts2_l.rec_set.all()
                for ls in s:
                    ss = ls.present
                    gifts2.append(ss)
            except:
                pass
        print(gifts1)
        print(gifts2)
        gifts1 = list(set(gifts1))
        gifts2 = list(set(gifts2))
        giftss = list(set(gifts1).union(set(gifts2)))
        conx = serializers.serialize("json", giftss[offset:offset+count])
        return HttpResponse(conx, content_type="application/json")

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

def obj_2_json(present, number):
    return {
        'present_id':present.id,
        'number':number,
        'name': present.name,
        "on_date": present.on_date.strftime('%Y-%m-%d %H:%M:%S'),
        "store_num": present.store_num,
        "status": present.status,
        "cost": (float)(present.cost),
        "hot": present.hot,
        "off": present.hot,
        "off_cost": (float)(present.off_cost),
        "url": present.url
    }

#done
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
            cart.append(obj_2_json(p.present, p.number))
        print(cart)
        conx = json.dumps(cart)
        conx2 = '{"error": 0, "car": ' + conx + '}'
        return HttpResponse(conx2, content_type="application/json")
    if request.method == 'POST':
        number = request.POST.get('number')
        present_id = request.POST.get('present_id')
        present = Present.objects.get(pk=present_id)
        user = User.objects.get(pk=user_id)
        car1 = Car.objects.filter(user=user, present=present)
        if car1:
            car1 = car1[0]
            car1.number = number
            car1.save()
        else:
            object = Car(user=user, number=number, present=present)
            object.save()
        return HttpResponse(json.dumps(context), content_type="application/json")
    if request.method == 'DELETE':
        delete = QueryDict(request.body)
        key = delete.get('present_id')
        if(key):
            #print(key)
            present = Present.objects.get(pk=key)
            user = User.objects.get(pk=user_id)
            object = Car.objects.filter(user=user, present=present)
            '''
            car = User.objects.filter(pk=user_id)[0].car_set.all()
            for c in car:
                if(c.present.id == key):
                    c.delete()
            '''
            if object:
                object = object[0]
                object.delete()
                context['error'] = 2
                return HttpResponse(json.dumps(context), content_type="application/json")
            else:
                context['error'] = 3
                return HttpResponse(json.dumps(context), content_type="application/json")
        else:
            context['error'] = 3
            return HttpResponse(json.dumps(context), content_type="application/json")
    if request.method == 'PUT':
        put = QueryDict(request.body)
        key = put.get('present_id')
        number = put.get('number')
        present = Present.objects.get(pk = key)
        user = User.objects.get(pk=user_id)
        object = Car.objects.filter(user=user, present=present)[0]
        object.number = number
        object.save()
        return HttpResponse(json.dumps(context), content_type="application/json")

#done
def orders(request, user_id):
    user = User.objects.get(pk=user_id)
    context = {
        'error': 0
    }
    if (not user) or ('USER_Id' not in request.session) or ('IS_LOGIN' not in request.session) \
            or (request.session['USER_Id'] != user_id):
        context['error'] = 1
        return HttpResponse(json.dumps(context), content_type="application/json")
    if request.method == 'GET':
        orderss = User.objects.get(pk=user_id).order_set.all()
        conx = serializers.serialize("json", orderss)
        conx2 = '{"error": 0, "car": ' + conx + '}'
        return HttpResponse(conx2, content_type="application/json")

#done
def order(request, user_id, order_id):
    user = User.objects.get(pk=user_id)
    context = {
        'error': 0
    }
    if (not user) or ('USER_Id' not in request.session) or ('IS_LOGIN' not in request.session) \
            or (request.session['USER_Id'] != user_id):
        context['error'] = 1
        return HttpResponse(json.dumps(context), content_type="application/json")
    if request.method=='GET':
        user = User.objects.get(pk=user_id)
        orderss = Order.objects.filter(user=user,pk=order_id)
        if orderss:
            orderss = orderss[0]
            orderes = orderss.oru_set.all()
            conx = serializers.serialize("json", orderes)
            conx2 = '{"error": 0, "car": ' + conx + '}'
            return HttpResponse(conx2, content_type="application/json")
        else:
            context['error']=1
            return HttpResponse(json.dumps(context), content_type="application/json")


def buy(request):
    context = {
        'error': 0
    }
    if ('IS_LOGIN' not in request.session or 'USER_Id' not in request.session):
        context['error'] = 1
        return HttpResponse(json.dumps(context), content_type="application/json")
    if request.method=='POST':
        user = User.objects.get(pk=request.session['USER_Id'])
        object_orders = Order(status = "操作成功",
                            receive_mark = 0,
                            user = user,
                            logistics = "null",
                            begin_date = datetime.datetime.now(),
                            sum_money = 0,
                            user_feedback = "null",
                            type = 0)
        object_orders.save()
        number = request.POST.getlist('number')
        present_id = request.POST.getlist('present_id')
        sum = 0
        for i in range(len(present_id)):

            present = Present.objects.get(pk=present_id[i])
            object_car = Car.objects.filter(present=present, user=user)
            if object_car:
                object_car.delete()
            count = number[i]
            price = (float)(present.cost)*(float)(number[i])
            order = object_orders
            object_order = Oru(present=present,count=count,price=price,order=order)
            object_order.save()
            sum += price
        object_orders.sum_money = sum
        object_orders.save()
        return HttpResponse(json.dumps(context), content_type="application/json")

#done
def search(request):
    if request.method == 'GET':
        count = request.GET.get('count')
        offset = request.GET.get('offset')
        q = request.GET.get('q')
        if not count:
            count = 10
        if not offset:
            offset = 0
        conx = ''
        if not q:
            giftss = Present.objects.all().order_by('hot')[offset:count+offset]
            conx = serializers.serialize("json", giftss)
        else:
            giftss = Present.objects.filter(name__icontains = q).order_by('hot')[offset:count+offset]
            conx = serializers.serialize("json", giftss)

        return HttpResponse(conx, content_type="application/json")


