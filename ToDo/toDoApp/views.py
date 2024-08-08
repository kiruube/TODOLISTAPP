from django.shortcuts import render,redirect
from .models import Task

# Create your views here.
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('index')
    return render(request, 'add_task.html')