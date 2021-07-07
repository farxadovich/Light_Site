from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)


class Comment(models.Model):
    author = models.ForeignKey()
    text = models.TextField(null=True)
    pub_date = models.
    tovar = models.ForeignKey(Tovar)



class Filial(models.Model):
    nomi = models.CharField(max_length=100)
    address = models.TextField()




class Tovar(models.Model):
    categoty = models.ForeignKey(blank=True)
    nomi = models.CharField(max_length=50)
    tarif = models.TextField(null=True)
    narxi = models.FloatField()
    image = models.ImageField(null=True)
    comments = models.TextField(null=True)
    rating = models.

class User(models.Model):
