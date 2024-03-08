from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from django.contrib.auth.decorators import login_required

#forms
from todo import forms
from todo.models import Task, Profile
# Create your views here.


def home(request):
    context = {}
    return render(request, 'todo/index.html', context )



@login_required
def task(request):
    profile = request.user.profile
    tasks = Task.objects.filter(profile=profile)

    context={
        'tasks':tasks,
    }
    return render(request, 'todo/todo.html', context)


def create_task(request):
    profile = request.user.profile
    get_title = request.POST.get('title__contains')
    task = Task.objects.create(profile=profile, title=get_title)

    tasks = Task.objects.filter(profile=profile)
    
    print(tasks)

    context={
        'tasks':tasks,
    }
    context={'tasks':tasks,
             
             }
    return render(request, 'todo/snippets/create-task.html', context)
    

def register(request):

    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login-page')
        
    else:
        form = forms.UserRegisterForm()


    context={
        'form':form,
    }
    return render(request, 'todo/register.html', context)

def check_user_availability(request):
    username = request.POST.get('username')
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse('<p style="color:red" > Not available </p>')
    
    else:
        return HttpResponse('<p style="color:green" > Available </p>')
   
