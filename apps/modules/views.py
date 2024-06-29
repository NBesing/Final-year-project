# views.py

from django.shortcuts import render
from .models import Module  # Adjust this import based on your actual app structure

def module_list(request):
    modules = Module.objects.all()  # Example query to fetch modules
    return render(request, 'includes/module_list.html', {'modules': modules})

def module_exercise(request):
    modules = Module.objects.all()
    return render(request, 'exercise/module_exercise.html', {'modules': modules})

def exercise_list(request):
    modules = Module.objects.all()
    return render(request, 'exercise/exercise_list.html', {'modules': modules})