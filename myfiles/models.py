from django.db import models

# Create your models here.
class Murojat(models.Model):
    username = models.CharField(max_length=30,null=True,blank=True)
    ism = models.CharField(max_length=30,null=True,blank=True)
    fam = models.CharField(max_length=30,null=True,blank=True)
    yosh = models.IntegerField()
    shaxar = models.CharField(max_length=30)
    matn = models.TextField()
    tel = models.CharField(max_length=30)
    tg_id= models.IntegerField()