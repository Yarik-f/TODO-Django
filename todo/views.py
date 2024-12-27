from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *

from .forms import TaskForm, RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

from rest_framework.viewsets import ModelViewSet
from .serializer import TaskSerializers

def test_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
        return redirect('task-list')
    else:
        form = TaskForm()
    return render(request, 'test.html', {'form': form})

def account_view(request):
    return render(request, 'profile/account.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Регистрация прошла успешно!')
        return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'profile/register.html', {'form': form})
def login_view(request):
    error_message = None
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('task_list')
        else:
            error_message = 'ХУЙНЯ'
    return render(request, 'profile/login.html', {'error': error_message})

def task_view(request):
    filter_option = request.GET.get('filter', 'public')
    if filter_option == 'my' and request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user)
    else:
        tasks = Task.objects.filter(is_public=True)

    return render(request, 'task_list.html', {'tasks': tasks, 'filter_option': filter_option})
def create_task(request):
    if request.method == 'POST':
        user_option = request.POST.get('user')
        title = request.POST.get('title')
        description = request.POST.get('description')
        time = request.POST.get('date_completed')
        if time:
            date_completed = datetime.strptime(time, '%Y-%m-%dT%H:%M')
        else:
            date_completed = datetime.now()
        task = Task.objects.create(title=title, description=description, date_completed=date_completed)
        if user_option:
            task.user = request.user
        else:
            task.is_public = True

        task.save()
        return redirect('task_list')
    return render(request, 'task_form.html', {'user': request.user})
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'task_confirm_delete.html', {'task': task})
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        user_option = request.POST.get('user')
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        time = request.POST.get('date_completed')
        if time:
            task.date_completed = datetime.strptime(time, '%Y-%m-%dT%H:%M')
        else:
            task.date_completed = None
        if user_option == 'my' and request.user.is_authenticated:
            task.user = request.user
        else:
            task.user = None
        task.save()
        return redirect('task_list')
    return render(request, 'task_form.html', {'task': task})
def toggle_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.status = not task.status
    task.save()
    return redirect('task_list')

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers


# def check_notifications(request):
#     new_notifications = Notification.objects.filter(read=False)
#     if new_notifications.exists():
#         new_notifications.update(read=True)
#         return JsonResponse({
#             "new_notifications": True,
#             "message": "Есть новые уведомления!"
#         })
#     return JsonResponse({"new_notifications": False})