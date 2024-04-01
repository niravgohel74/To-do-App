from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    todos = Todo.objects.order_by('-id')
    context = {
        'todos': todos
    }
    return render(request, "index.html", context)

def create_todo(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        Todo.objects.create(
            title = title,
            description = description
        )
    return redirect('index')

def complete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('index')

def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')