from django.shortcuts import render
from .models import Level

def level_list(request):
    levels = Level.objects.all()
    return render(request, 'levels/level_list.html', {'levels': levels})

def level_detail(request, pk):
    level = Level.objects.get(pk=pk)
    return render(request, 'levels/level_detail.html', {'level': level})
