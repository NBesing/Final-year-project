# views.py

from django.shortcuts import render, get_object_or_404
from .models import Module, ModuleExercise # Import your models here

def module_list(request):
    modules = Module.objects.all()
    return render(request, 'includes/module_list.html', {'modules': modules})

def module_exercise(request, module_id):
    try:
        module = get_object_or_404(Module, pk=module_id)
        exercises = ModuleExercise.objects.filter(module=module)
        
        context = {
            'module': module,
            'exercises': exercises,
        }
        return render(request, 'exercise/module_exercise.html', context)
    except Module.DoesNotExist:
        return render(request, 'exercise/module_exercise.html', {'error': 'Module not found'})

def exercise_list(request):
    modules = Module.objects.all()
    return render(request, 'exercise/exercise_list.html', {'modules': modules})
