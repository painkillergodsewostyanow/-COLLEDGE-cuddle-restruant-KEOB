from django.shortcuts import render
from django.http import HttpResponse
from main.models import Food


def index(request):
    return render(request, 'main/index.html')


def menu(request):
    return render(request, 'main/menu.html')


def reg_user(request):
    f = Food.objects.all()
    return render(request, 'main/menu.html', {'food': f})

