from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    context = {}
    return render(request, 'todo/index.html', context )



def register(request):
    context={}
    return render(request, 'todo/register.html', context)