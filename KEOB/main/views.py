from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from .forms import *
from main.models import Food, Post
from django.urls import reverse_lazy
from django.shortcuts import redirect
import random


def index(request):
    return render(request, 'main/index.html')


def menu(request):
    food = {}
    for i in Food.objects.all():
        food[i.pk] = i
    return render(request, 'main/menu.html', food)


def comment(request):
    comments = Post.objects.all()
    return render(request, 'main/comment.html', {'com': comments})


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


def logout_user(request):
    logout(request)
    return redirect('home')


def add_page(request):
    good_words = Post.objects.values_list('txt', flat=True).distinct()
    if len(good_words) != 0:
        good_word_by_default = good_words[random.randint(0, len(good_words)-1)]
    else:
        good_word_by_default = ''
    if request.method == 'POST':
        form = AddComment(request.POST)
        if form.is_valid():
            form.save()
            return redirect('com')
    else:
        form = form = AddComment(initial={'name': request.user.username, 'txt': str(good_word_by_default)})
    return render(request, 'main/add_comment.html', {'form': form})


def delivery(request):
    return render(request, 'main/delivery.html')

