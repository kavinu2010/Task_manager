from django.shortcuts import render, redirect
from .models import Task

def index(request):
    if request.method == 'POST':
        # Get task details from form
        task_name = request.POST.get('task_name')
        task_time = request.POST.get('task_time')
        if task_name and task_time:
            Task.objects.create(task_name=task_name, time=task_time)

    tasks = Task.objects.all()  # Fetch all tasks
    return render(request, 'index.html', {'tasks': tasks})

def delete_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        task.delete()
    except Task.DoesNotExist:
        pass
    return redirect('/')
