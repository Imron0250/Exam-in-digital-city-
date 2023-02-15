from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField()


class ProductPhoto(models.Model):
    photo = models.ImageField()


class ProductInfo(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ManyToManyField(ProductPhoto)
    is_new = models.BooleanField(default=True)
    rating = models.IntegerField(default=0)
    price = models.IntegerField()
    bonus = models.IntegerField()
    description = models.TextField()
    availability = models.BooleanField(default=True)
    info = models.ManyToManyField(ProductInfo)
    in_slider = models.BooleanField(default=True)
    in_ad = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Service(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=255)
    text = models.CharField(max_length=255)


class Blog(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    full_text = models.TextField()


class Emails(models.Model):
    email = models.EmailField()


class Info(models.Model):
    phone1 = models.CharField(max_length=255)
    phone2 = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    logo = models.ImageField()
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)


class Team(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)


class ClientSays(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    image = models.ImageField()


class Partner(models.Model):
    image = models.ImageField()


class OurStories(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    video = models.FileField()


class Faq(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)


class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateField()
    total_price = models.IntegerField()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    price = models.IntegerField()


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)