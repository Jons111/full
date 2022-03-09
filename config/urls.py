"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from config import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from myapp.views import *

urlpatterns = [
    path('adminjon/', admin.site.urls),
    path('', home, name = 'home'),
    path('about/', about, name = 'about'),
    path('codes/', codes, name = 'codes'),
    path('faq/', faq, name = 'faq'),
    path('icons/', icons, name = 'icons'),
    path('mail/', mail, name = 'mail'),
    path('products/', products, name = 'products'),
    path('products1/', products1, name = 'products1'),
    path('products2/', products2, name = 'products2'),
    path('single/', single, name = 'single'),
    path('products_sort/<str:id>', products, name = 'products_sort'),
    path('products_sort1/<str:id>', products1, name = 'products_sort1'),
    path('products_sort2/<str:id>', products2, name = 'products_sort2'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIAFILES_DIRS)
