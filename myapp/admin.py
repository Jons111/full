from django.contrib import admin
from myapp.models import *


# Register your models here.

class AdminMail(admin.ModelAdmin):
    list_display = ['id', 'name', 'tel', 'email', 'message']


admin.site.register(Mail, AdminMail)


class AdminNewsletter(admin.ModelAdmin):
    list_display = ['id', 'email']


admin.site.register(Newslettter, AdminNewsletter)


class AdminMobile(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Mobile, AdminMobile)


class AdminAccessories(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Accessories, AdminAccessories)


class AdminHome(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Home, AdminHome)


class AdminColor(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Color, AdminColor)


class AdminMobile_products(admin.ModelAdmin):
    list_display = ['id', 'name', 'newprice', 'type', 'color', 'image',]


admin.site.register(Mobile_products, AdminMobile_products)


class AdminAccesuar_products(admin.ModelAdmin):
    list_display = ['id', 'name', 'newprice', 'type', 'color', 'image',]


admin.site.register(Accesuar_products, AdminAccesuar_products)


class AdminHome_products(admin.ModelAdmin):
    list_display = ['id', 'name', 'newprice', 'type', 'color', 'image',]


admin.site.register(Home_products, AdminHome_products)


class AdminBasket_mobile(admin.ModelAdmin):
    list_display = ['id', 'name', 'newprice', 'amount', 'type']


admin.site.register(Basket_mobile, AdminBasket_mobile)

class AdminBasket_accesories(admin.ModelAdmin):
    list_display = ['id', 'name', 'newprice', 'amount', 'type']

admin.site.register(Basket_accesuars, AdminBasket_accesories)

class AdminBasket_home(admin.ModelAdmin):
    list_display = ['id', 'name', 'newprice', 'amount', 'type']

admin.site.register(Basket_home, AdminBasket_home)

class AdminSingle_review(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'tel', 'message']
admin.site.register(Single_review, AdminSingle_review)

class AdminSign_up(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'password', 'confirm_password']
admin.site.register(Sing_up, AdminSign_up)

class AdminSing_in(admin.ModelAdmin):
    list_display = ['id', 'email', 'password']
admin.site.register(Sign_in, AdminSing_in)