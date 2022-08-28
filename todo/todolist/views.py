from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import TodoForm
from .models import Todo
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

def home(request):
    return render(request, 'todolist/home.html')
@login_required
def todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo-view')
    else:
        form = TodoForm()
    context = {'form': form}
    return render(request, 'todolist/todo.html', context)
@login_required
def todo_view(request):
    todos = Todo.objects.all()
    context = {'todos': todos}
    return render(request, 'todolist/todo-view.html', context)