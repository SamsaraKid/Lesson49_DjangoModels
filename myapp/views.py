from django.shortcuts import render, redirect
from .models import Persona
from .myforms import PersonForm


def index(req):
    form = PersonForm()
    bd = Persona.objects.all()
    return render(req, 'index.html', context={'form': form, 'database': bd})


def add1(req):
    man = Persona()
    man.name = 'Igor'
    man.age = 22
    man.save()
    man2 = Persona.objects.create(name='Vlad', age='13')
    return redirect('index')


def create(req):
    if req.POST:
        man = Persona()
        man.name = req.POST.get('name')
        man.age = req.POST.get('age')
        man.save()
        return redirect('index')


def del1(req, id):
    man = Persona.objects.get(id=id)
    man.delete()
    return redirect('index')