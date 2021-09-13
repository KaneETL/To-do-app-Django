from django import forms
from django.http import response
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Todo
from todo.forms import TodoForm


def todo_list(request):
  
    todo_objects = Todo.objects.all()
    form = TodoForm(request.POST or None)
    context = {
        'todo_objects': todo_objects,
        'form':form
    }
    if form.is_valid():
        todo = form.save(commit=False)
        todo.user = request.user
        todo.save()

    
    
    return render(request, "mainpage/home.html", context)

def todo_complete(request):
    




