from django.shortcuts import render, get_object_or_404
from .models import Lesson

def lesson_list(request):
    lessons = Lesson.objects.all()
    return render(request, 'lessons/lesson_list.html', {'lessons': lessons})

def lesson_detail(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    subtopics = lesson.content.get('subtopics', [])  # Accessing subtopics from content field
    return render(request, 'lesson_detail.html', {'lesson': lesson, 'subtopics': subtopics})

def level_selection(request):
    return render(request, 'level_selection.html')
