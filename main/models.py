from django.db import models


class Info(models.Model):
    comp_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    img = models.ImageField(upload_to="InfoIMG")


class Services(models.Model):
    img = models.ImageField(upload_to="ServicesIMG")
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)


class About(models.Model):
    img = models.ImageField(upload_to="AboutIMG")
    text = models.CharField(max_length=500)
    text1 = models.CharField(max_length=500)


class Portfolio(models.Model):
    img = models.ImageField(upload_to="AboutIMG")
    tite = models.CharField(max_length=255)


class Testimonials(models.Model):
    name = models.CharField(max_length=255)
    tite = models.CharField(max_length=255)


class Clients(models.Model):
    img = models.ImageField(upload_to="ClientsIMG")
    name = models.CharField(max_length=255)


class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
