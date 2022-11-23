from django.shortcuts import render
from django.http import HttpResponse

from main.models import Food


def index(request):
    return render(request, 'main/index.html')


def menu(request):
    food = {}
    for i in Food.objects.all():
        food[i.pk] = i
    print(food.values())
    return render(request, 'main/menu.html', food)


def reg_user(request):
    return render(request, 'main/menu.html')
