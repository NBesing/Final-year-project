# views.py

from django.shortcuts import render
from .models import Module  # Adjust this import based on your actual app structure

def module_list(request):
    modules = Module.objects.all()  # Example query to fetch modules
    return render(request, 'includes/module_list.html', {'modules': modules})

def module_exercise(request):
    modules = Module.objects.all()
   

    try:
            module = Module.objects.get(id=module_id)
            exercises = Exercise.objects.filter(module=module)
            questions = Question.objects.filter(exercise__in=exercises)

            context = {
                'module': module,
                'questions': questions,
            }
            return render(request, 'exercise_detail.html', context)
    except Module.DoesNotExist:
            # Handle case where module with given ID does not exist
            return render(request, 'exercise_detail.html', {'error': 'Module not found'})

def exercise_list(request):
    modules = Module.objects.all()
    return render(request, 'exercise/exercise_list.html', {'modules': modules})