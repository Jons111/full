from django.db import models


# Create your models here.
class Mail(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    tel = models.IntegerField()
    message = models.TextField()


class Newslettter(models.Model):
    email = models.EmailField()


class Mobile(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Accessories(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Home(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Mobile_products(models.Model):
    name = models.CharField(max_length=20)
    newprice = models.IntegerField()
    oldprice = models.IntegerField()
    ranking = models.IntegerField()
    type = models.ForeignKey(Mobile, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/')
    amount = models.IntegerField(null=True)


class Accesuar_products(models.Model):
    name = models.CharField(max_length=20)
    newprice = models.IntegerField()
    oldprice = models.IntegerField()
    ranking = models.IntegerField()
    type = models.ForeignKey(Accessories, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/')
    amount = models.IntegerField(null=True)


class Home_products(models.Model):
    name = models.CharField(max_length=20)
    newprice = models.IntegerField()
    oldprice = models.IntegerField()
    ranking = models.IntegerField()
    type = models.ForeignKey(Home, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/')
    amount = models.IntegerField(null=True)

class Basket_mobile(models.Model):
    name =  models.CharField(max_length=20)
    newprice = models.IntegerField()
    amount = models.IntegerField(null=True, default=1)
    type = models.ForeignKey(Mobile, on_delete=models.CASCADE, null=True)

class Basket_accesuars(models.Model):
    name =  models.CharField(max_length=20)
    newprice = models.IntegerField()
    amount = models.IntegerField(null=True, default=1)
    type = models.ForeignKey(Accessories, on_delete=models.CASCADE, null=True)

class Basket_home(models.Model):
    name =  models.CharField(max_length=20)
    newprice = models.IntegerField()
    amount = models.IntegerField(null=True, default=1)
    type = models.ForeignKey(Home, on_delete=models.CASCADE, null=True)


class Single_review(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    tel = models.IntegerField()
    message = models.TextField()

class Sing_up(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=8, null=True)
    confirm_password = models.CharField(max_length=8, null=True)

class Sign_in(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=10, null=True)