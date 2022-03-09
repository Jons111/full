from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    if 'EmailHome' in request.POST:
        email = request.POST.get('EmailHome')
        emails = Newslettter.objects.all()
        id = [0]
        for i in emails:
            id.append(i.id)
        Newslettter(max(id)+1, email).save()
    if 'Name_Signup' in request.POST:
        name = request.POST.get('Name_Signup')
        email = request.POST.get('Email_Signup')
        password = request.POST.get('Password_Signup')
        confirm_password = request.POST.get('Password_Confirm_Signup')
        s = 'Plese, make sure your confirm password is equal to your password!'
        if confirm_password != password:
            confirm_password = request.POST.get('Password_Confirm_Signup')
        ids = [0]
        users = Sing_up.objects.all()
        for a in users:
            ids.append(a.id)
        Sing_up(max(ids)+1, name, email, password, confirm_password, ).save()
    elif 'Name_Signin' in request.POST:
        emailSS = request.POST.get('Name_Signin')
        passwordSS = request.POST.get('Password_Signin')
        idss = [0]
        userss = Sign_in.objects.all()
        for user in userss:
            idss.append(user.id)
        Sign_in(67, emailSS, passwordSS).save()
    mobillar = Mobile.objects.all()
    accesuars = Accessories.objects.all()
    home = Home.objects.all()
    products = Mobile_products.objects.all()
    return render(request, 'index.html', {"mobiles": mobillar, "accesuars": accesuars, "home": home, 'product': products})

def about(request):
    if 'EmailAbout' in request.POST:
        email = request.POST.get('EmailAbout')
        emails = Newslettter.objects.all()
        id = [0]
        for i in emails:
            id.append(i.id)
        Newslettter(max(id)+1, email).save()
    if 'Email' in request.POST:
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        users = Sign_in.objetcs.all()
        ids = [0]
        for user in users:
            ids.append(user.id)
        Sign_in(max(ids)+1, email, password).save()
    mobillar = Mobile.objects.all()
    accesuars = Accessories.objects.all()
    home = Home.objects.all()
    return render(request, 'about.html', {"mobiles": mobillar, "accesuars": accesuars, "home": home})

def codes(request):
    if 'EmailCodes' in request.POST:
        emaill = request.POST.get('EmailCodes')
        email = Newslettter.objects.all()
        id = [0]
        for i in email:
            id.append(i.id)
        Newslettter(max(id)+1, emaill).save()
    mobillar = Mobile.objects.all()
    accesuars = Accessories.objects.all()
    home = Home.objects.all()
    return render(request, 'codes.html', {"mobiles": mobillar, "accesuars": accesuars, "home": home})

def faq(request):
    if 'EmailFaq' in request.POST:
        email = request.POST.get('EmailFaq')
        emails = Newslettter.objects.all()
        id = [0]
        for i in emails:
            id.append(i.id)
        Newslettter(max(id)+1, email).save()
    mobillar = Mobile.objects.all()
    accesuars = Accessories.objects.all()
    home = Home.objects.all()
    return render(request, 'faq.html', {"mobiles": mobillar, "accesuars": accesuars, "home": home})

def icons(request):
    if 'EmailIcons' in request.POST:
        email = request.POST.get('EmailIcons')
        emails = Newslettter.objects.all()
        id = [0]
        for i in emails:
            id.append(i.id)
        Newslettter(max(id)+1, email).save()
    mobillar = Mobile.objects.all()
    accesuars = Accessories.objects.all()
    home = Home.objects.all()
    return render(request, 'icons.html', {"mobiles": mobillar, "accesuars": accesuars, "home": home})



def products(request, id = 0):
    if 'EmailProducts' in request.POST:
        email = request.POST.get('EmailProducts')
        emails = Newslettter.objects.all()
        id = [0]
        for i in emails:
            id.append(i.id)
        Newslettter(max(id) + 1, email).save()
    mobillar = Mobile.objects.all()
    accesuars = Accessories.objects.all()
    home = Home.objects.all()
    if id != 0:
        tur = Mobile.objects.get(id = id)
        produccts = Mobile_products.objects.filter(type = tur)
    else:
        produccts = Mobile_products.objects.all()
    colors = Color.objects.all()

    if "cmd" in request.POST:
        type = request.POST.get('cmd')
        amount = request.POST.get('add')
        name = request.POST.get('w3ls_item')
        price = request.POST.get('amount')
        ids = [0]
        mobiles = Basket_mobile.objects.all()
        for mobile in mobiles:
            ids.append(mobile.id)

        Basket_mobile(max(ids)+1, name, price, amount, type).save()

    return render(request, 'products.html', {"mobiles": mobillar, "accesuars": accesuars, "home": home, 'product': produccts, 'color': colors})

def products1(request, id=0):
    if 'EmailProducts1' in request.POST:
        email = request.POST.get('EmailProducts1')
        emails = Newslettter.objects.all()
        id = [0]
        for i in emails:
            id.append(i.id)
        Newslettter(max(id)+1, email).save()
    mobillar = Mobile.objects.all()
    accesuars = Accessories.objects.all()
    home = Home.objects.all()
    if id  != 0:
        tur2 = Accessories.objects.get(id = id)
        products_acc = Accesuar_products.objects.filter(type = tur2)
    else:
        products_acc = Accesuar_products.objects.all()

    if "cmd" in request.POST:
        type = request.POST.get('cmd')
        amount = request.POST.get('add')
        name = request.POST.get('w3ls_item')
        price = request.POST.get('amount')
        ids = [0]
        mobiles = Basket_accesuars.objects.all()
        for mobile in mobiles:
            ids.append(mobile.id)

        Basket_accesuars(max(ids)+1, name, price, amount, type).save()

    return render(request, 'products1.html', {"mobiles": mobillar, "accesuars": accesuars, "home": home, 'product_acc':products_acc})

def products2(request, id = 0):
    if 'EmailProducts2' in request.POST:
        email = request.POST.get('EmailProducts2')
        emails = Newslettter.objects.all()
        id = [0]
        for i in emails:
            id.append(i.id)
        Newslettter(max(id)+1, email).save()
    mobillar = Mobile.objects.all()
    accesuars = Accessories.objects.all()
    home = Home.objects.all()
    if id != 0:
        tur1 = Home.objects.get(id = id)
        product_home = Home_products.objects.filter(type = tur1)
    else:
        product_home = Home_products.objects.all()

    if "cmd" in request.POST:
        type = request.POST.get('cmd')

        amount = request.POST.get('add')
        name = request.POST.get('w3ls_item')
        price = request.POST.get('amount')
        ids = [0]
        mobiles = Basket_home.objects.all()
        for mobile in mobiles:
            ids.append(mobile.id)

        Basket_home(max(ids)+1, name, price, amount,type).save()
    return render(request, 'products2.html', {"mobiles": mobillar, "accesuars": accesuars, "home": home, 'product_home': product_home})

def single(request):
    if 'Name' in request.POST:
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        tel = request.POST.get('Telephone')
        message = request.POST.get('Review')
        idlar = [0]
        emaillar = Single_review.objects.all()
        for e in emaillar:
            idlar.append(e.id)
        Single_review(max(idlar)+1, name, email, tel, message).save()
    elif 'EmailSingle' in request.POST:
        email = request.POST.get('EmailSingle')
        emails = Newslettter.objects.all()
        id = [0]
        for i in emails:
            id.append(i.id)
        Newslettter(max(id)+1, email).save()
    mobillar = Mobile.objects.all()
    accesuars = Accessories.objects.all()
    home = Home.objects.all()
    return render(request, 'single.html', {"mobiles": mobillar, "accesuars": accesuars, "home": home})

def mail(request):
    if 'Name' in request.POST:
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        tel = request.POST.get('Telephone')
        message = request.POST.get('message')

        idlar = [0]
        emaillar = Mail.objects.all()
        for e in emaillar:
            idlar.append(e.id)
        Mail(max(idlar)+1, name, email, tel, message).save()
    elif 'Email' in request.POST:
        email = request.POST.get('Email')
        emails = Newslettter.objects.all()
        id = [0]
        for a in emails:
            id.append(a.id)
        Newslettter(max(id)+1, email).save()
    mobillar = Mobile.objects.all()
    accesuars = Accessories.objects.all()
    home = Home.objects.all()
    return render(request, 'mail.html', {"mobiles": mobillar, "accesuars": accesuars, "home": home})