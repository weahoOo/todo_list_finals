from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Task

def home(request):
    tasks = Task.objects.filter(is_done=False).order_by('-created_at')
    return render(request, 'todo/home.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
    return redirect('home')

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            task.title = title
            task.save()
        return redirect('home')
    return JsonResponse({'error': 'Invalid request'}, status=400)

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('home')

def mark_done(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_done = True
    task.save()
    return redirect('home')
