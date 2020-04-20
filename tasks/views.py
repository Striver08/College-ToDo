from django.shortcuts import render
from django.http import HttpResponse
from .models import Task


def home(request):
    
    task = Task.objects.all()

    return render(request, 'tasks/home.html', {'tasks' : task})