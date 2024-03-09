from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

#security
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

#forms
from todo import forms
from todo.models import Task, Profile
# Create your views here.

#secuirty functions



#secuirty functions

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

@login_required
def create_task(request):
    profile = request.user.profile
    get_title = request.POST.get('title__contains')
    task = Task.objects.create(profile=profile, title=get_title)
    

    tasks = Task.objects.filter(profile=profile)
    
    

    context={
        'tasks':tasks,
    }
    
    return render(request, 'todo/snippets/create-task.html', context)

@login_required
def complete_task(request, pk):
    #here im retrieving currrent profile, and the task we want to update
    profile = request.user.profile
    task = get_object_or_404(Task, pk=pk)
    
    #first check that the profile trying to modify the task is the author
    # if the task is completed then we chang to false, and if its not completed, then we change to completed
    if task.profile == profile:
        if task.completed:
            task.completed = False
        else:
            task.completed = True
    else:
        return render(request, 'todo/no-access.html')

        

    #next we save that, and we also retrive all the tasks to render them
    task.save()
    tasks = Task.objects.filter(profile=profile)

    context={
        'tasks':tasks,
    }
    return render(request, 'todo/snippets/create-task.html', context)



@login_required
def delete_task(request, pk):
    #we get the profile, and the task 
    profile = request.user.profile
    task = get_object_or_404(Task, pk=pk)
    
    #we check if the tasks profile matches the current profile and if it does then we have access to delete
    #if it doesnt, then that means idk how they are trying to delete!
    if task.profile == profile:
        task.delete()
    else:
        return render(request, 'todo/no-access.html')
    
    
    tasks = Task.objects.filter(profile=profile)

    context={'tasks':tasks}

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
   
