from django.db import models


class Persona(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    town = models.CharField(max_length=15, null=True, blank=True)


class Company(models.Model):
    name = models.CharField(max_length=10)
    year = models.IntegerField()



class Product(models.Model):
    title = models.CharField(max_length=30)
    price = models.DecimalField(decimal_places=2, max_digits=4)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
