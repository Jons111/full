from django.contrib import admin
from myfiles.models import Murojat
# Register your models here.
class AdminM(admin.ModelAdmin):
    list_display = ['id','username','ism','matn','tel','shaxar','tg_id']
admin.site.register(Murojat,AdminM)