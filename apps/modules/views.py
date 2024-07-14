# views.py
import random
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Module, ModuleExercise # Import your models here
import json  # Import the json module

def module_list(request):
    modules = Module.objects.all()
    return render(request, 'includes/module_list.html', {'modules': modules})


def module_exercise(request, module_id):
    try:
        module = get_object_or_404(Module, pk=module_id)
        exercises = list(module.moduleexercise_set.all().values('id', 'title', 'content'))

        random.shuffle(exercises)
        selected_exercises = exercises[:10]  
        
        context = {
            'module': module,
            'exercises_json': json.dumps(exercises),  # Convert exercises to JSON format
            
        }
        return render(request, 'exercise/module_exercise.html', context)
    except Module.DoesNotExist:
        return render(request, 'exercise/module_exercise.html', {'error': 'Module not found'})
    
def exercise_detail_view(request, exercise_id):
    try:
        exercise = ModuleExercise.objects.get(id=exercise_id)
        exercise_data = {
            'id': exercise.id,
            'content': exercise.content,
            'hints': exercise.hints.split('\n') if exercise.hints else []  # Split hints by newline if stored as multiline text
        }
        return JsonResponse(exercise_data)
    except ModuleExercise.DoesNotExist:
        return JsonResponse({'error': 'Exercise not found'}, status=404)

def exercise_list(request):
    modules = Module.objects.all()
    return render(request, 'exercise/exercise_list.html', {'modules': modules})
