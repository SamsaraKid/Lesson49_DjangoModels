from django.shortcuts import render, redirect
from .models import *
from .myforms import PersonForm


def index(req):
    form = PersonForm()
    bd = Persona.objects.all()
    print(Persona.objects.get(id=9).name, Persona.objects.get(id=9).age)
    print('========================')
    for p in Persona.objects.all():
        print(p.id, p.name, p.age)
    print('========================')
    igors = Persona.objects.filter(name='Igor')
    print(igors.values())
    print(igors.values_list())
    print(igors.in_bulk())
    print(igors[0].id)
    print('========================')
    excl = Persona.objects.exclude(name='Vlad')
    print(excl.values_list())
    igors_excl = Persona.objects.filter(name='Igor').exclude(age=22)
    print(igors_excl)

    k1 = Product.objects.create(title='confeta', price=50.0, company_id=2)
    k2 = Product.objects.create(title='confetaBIG', price=15.0, company_id=2)
    print(k2.company.name)
    chokos = Product.objects.filter(company__name='Mars')
    print(chokos.values_list())
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


def edit1(req, id):
    man = Persona.objects.get(id=id)
    anketa = PersonForm
    data = {'form': anketa}
    if req.POST:
        man.name = req.POST['name']
        man.age = req.POST['age']
        man.save()
        return redirect('index')
    else:
        return render(req, 'edit.html', context=data)


def del1(req, id):
    man = Persona.objects.get(id=id)
    man.delete()
    return redirect('index')