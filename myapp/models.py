from django.db import models


class Persona(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()