from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from main.models import Food
from django.urls import reverse_lazy


def index(request):
    return render(request, 'main/index.html')


def menu(request):
    food = {}
    for i in Food.objects.all():
        food[i.pk] = i
    return render(request, 'main/menu.html', food)


class reg(CreateView):
    form_class = RegUser
    template_name = 'main/reg.html'
    success_url = reverse_lazy('log')

    def get_context_date(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()) + list(c_def.items()))


class log_in(LoginView):
    form_class = LogUser
    template_name = 'main/log_in.html'

    def get_context_date(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')
