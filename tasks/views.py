from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from .forms import TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    title = "Django CRUD APP"
    return render(request, 'home.html', {
        'title': title
    })


def signup(request):
    title = "SignUp"
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'title': title,
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except:
                return render(request, 'signup.html', {
                    'response': 'User already exist',
                    'form': UserCreationForm
                })
        return render(request, 'signup.html', {
            'response': 'Passwords does not match',
            'form': UserCreationForm
        })

@login_required
def tasks(request):
    titulo = 'Tareas'
    tasks = Task.objects.filter(user = request.user)
    return render(request, 'tasks.html', {
        'title': titulo,
        'tasks': tasks
    })

@login_required
def signOff(request):
    logout(request)
    return redirect('home')


def signIn(request):
    if request.method == 'GET':
        return render(request, 'signIn.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'signIn.html', {
            'form': AuthenticationForm,
            'error': 'Username or password is incorrect'
        })
        else:
            login (request, user)
            return redirect('tasks')

@login_required
def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form': TaskForm
        })
    else:
        form = TaskForm(request.POST)
        new_task = form.save(commit=False)
        new_task.user = request.user
        new_task.save()
        return redirect('tasks')

@login_required
def task_detail(request, task_id):
    if request.method == "GET":
        task = get_object_or_404(Task, pk = task_id, user = request.user)
        form = TaskForm(instance=task)
        return render(request, 'task_detail.html', {
            'task': task,
            'form': form
        })
    else:
        task = get_object_or_404(Task,pk=task_id)
        form = TaskForm(request.POST, instance=task)
        form.save()
        return redirect('tasks')

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk = task_id, user = request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
