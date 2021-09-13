from django.http import response
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Todo



def todo_list(request):
    todo_objects = Todo.objects.all()
    context = {
        'todo_objects': todo_objects
    }
    response.user.todolist.all.create(name=n)
    return render(request, "mainpage/home.html", context)

class homeview(TemplateView):
    template_name = 'mainpage/home.html'
