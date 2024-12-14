# from django.shortcuts import render , redirect
# from .models import NewTask

# # Create your views here.
# def saveinfo(request):
#   if request.method=='POST':
#     AddTask=request.POST('addtask')
#     time=request.POST('time')
#     add=NewTask(AddTask=AddTask,time=time)
#     add.save()
#   Add=NewTask.objects.all()
#   return render(request,'index.html',{'Add':Add})

# def index(request):
#   Add=NewTask.objects.all()
#   return render(request,'index.html',{'Add':Add})

# def Delete(rerquest,id):
#   New=NewTask.objects.get(id=id)
#   New.delete()
#   return redirect('/')


from django.shortcuts import render, redirect
from .models import NewTask

# Create your views here.
def save_task(request):
    if request.method == 'POST':
        add_task = request.POST.get('addtask')  # Use .get() to avoid errors if key is missing
        time = request.POST.get('time')
        if add_task and time:  # Validate that both fields are provided
            new_task = NewTask(AddTask=add_task, time=time)
            new_task.save()
        return redirect('/')  # Redirect after saving to prevent form resubmission
    
    tasks = NewTask.objects.all()
    return render(request, 'index.html', {'tasks': tasks})  # Pass tasks for rendering

def index(request):
    tasks = NewTask.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def delete_task(request, id):
    try:
        task = NewTask.objects.get(id=id)
        task.delete()
    except NewTask.DoesNotExist:
        pass  # Optionally handle the case where the task does not exist
    return redirect('/')



                    