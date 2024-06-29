from django.shortcuts import render
from .models import Progress, Grade

def progress_list(request):
    progress = Progress.objects.all()
    return render(request, 'progress/progress_list.html', {'progress': progress})

def grade_list(request):
    grades = Grade.objects.all()
    return render(request, 'progress/grade_list.html', {'grades': grades})
