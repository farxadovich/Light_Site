from django.db import models
from django.contrib.auth.models import User, Group


class Category(models.Model):
    name = models.CharField(max_length=100)


class Comment(models.Model):
    author = models.ForeignKey(on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateTimeField()
    tovar = models.ForeignKey('Tovar', on_delete=models.CASCADE)



class Filial(models.Model):
    nomi = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    open_time = models.DateTimeField()
    close_time = models.DateTimeField()
    location = models.CharField(max_length=100)




class Tovar(models.Model):
    categoty = models.ForeignKey(Category, on_delete=models.CASCADE)
    nomi = models.CharField(max_length=50)
    tarif = models.TextField()
    narxi = models.FloatField()
    image = models.ImageField()
    comments = models.TextField(Comment, on_delete=models.CASCADE)
    reyting = models.ForeignKey()
    data_time = models.DateTimeField()
    creator = models.ForeignKey( on_delete=models.CASCADE)
    in_sale = models.ForeignKey('Sale', on_delete=models.CASCADE)
    sale_price = models.FloatField()
    ombor = models.ForeignKey(Filial, on_delete=models.CASCADE)

class Odam(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    basket = models.ForeignKey('Tovar', on_delete=models.CASCADE)
    orders = models.ForeignKey('order', on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    join_data = models.DateTimeField()
    contact = models.CharField(max_length=100)


class Order(models.Model):
    user = models.ForeignKey(Odam, on_delete=models.CASCADE)
    tovarlar = models.ForeignKey("Tovar", on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    total_price = models.FloatField()
    otziv = models.TextField()
    address = models.CharField(null=True)
    contact = models.CharField(null=True)
    status = models.BooleanField()

class Sell(models.Model):
    name = models.CharField(max_length=200)
    tovar = models.ForeignKey("Tovar", on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


class Admin(models.Model):
    name = models.CharField(max_length=19)
    password = models.CharField(max_length=19)
    join_date = models.DateTimeField()
    contact = models.CharField(max_length=100)


