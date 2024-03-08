from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

#forms
from todo import forms

# Create your views here.


def home(request):
    context = {}
    return render(request, 'todo/index.html', context )



def register(request):

    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home-page')
        
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
   
