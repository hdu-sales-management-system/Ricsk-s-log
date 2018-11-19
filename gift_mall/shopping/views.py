from django.shortcuts import render

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        user = User.objects.filter(username = username, password = pwd)
        context = {
            'user':null,
            'log_status': 0
        }
        request.session['IS_LOGIN'] = False
        request.session['USER_ID'] = user.id
        if user:
            context['user'] = user
            context['log_status'] = 1
            request.session['IS_LOGIN'] = True
            return render(request, request.path, context)
        else:
            return render(request, request.path, context)
    return render(request, request.path, context)


def logout(request):
    del request.session["IS_LOGIN"]
    del request.session["USER_ID"]
    render(request, request.path, context)


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        address = request.POST.get('address')
        birthday = request.POST.get('birthday')
        nickname = request.POST.get('nickname')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        user = User.objects.filter(username=username, password=pwd)
        context = {'re_true': 0}
        if username and pwd and not user:
            u = User(username=username,
                     password=pwd,
                     address=address,
                     birthday=birthday,
                     nickname=nickname,
                     gender=gender,
                     phone=phone)
            u.save()
            context['re_true'] = 1
        else:
            context['re_true'] = 0
        render(request, request.path, context)


def gifts(request):
    if request.method == 'GET':


def tags(request):
    return

def categorise(request):
    return

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
