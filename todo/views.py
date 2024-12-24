from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from .models import *

from rest_framework.viewsets import ModelViewSet
from .serializer import TaskSerializers

def task_view(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})
def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        time = request.POST.get('date_completed')
        if time:
            date_completed = datetime.strptime(time, '%Y-%m-%dT%H:%M')
        else:
            date_completed = datetime.now()
        Task.objects.create(title=title, description=description, date_completed=date_completed)
        return redirect('task_list')
    return render(request, 'task_form.html')
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'task_confirm_delete.html', {'task': task})
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        time = request.POST.get('date_completed')
        if time:
            task.date_completed = datetime.strptime(time, '%Y-%m-%dT%H:%M')
        else:
            task.date_completed = None
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