from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def index(request):
   tasks = Task.objects.all()
   return render(request, 'premium/index.html', {'title': 'Bezarre_kz', 'tasks': tasks})


def about(request):
    return render(request, 'premium/about.html')


def ice(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('flash')
    form = TaskForm()
    context = {
        'form' : form
    }
    return render(request, 'premium/ice.html', context)


def flash(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались, Добро пожаловать в Bezarre')


    context={'form': form}
    return render(request, 'premium/flash.html', context)

def login(request):
    return render(request, 'premium/login.html')



