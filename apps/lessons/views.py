from django.shortcuts import render, get_object_or_404
from .models import Lesson

def lesson_list(request):
    lessons = Lesson.objects.all()
    return render(request, 'lessons/lesson_list.html', {'lessons': lessons})

def lesson_detail(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    subtopics = lesson.content.get('subtopics', []) 
    
    # Get IDs of previous and next lessons
    previous_lesson_id = lesson.get_previous_lesson_id()
    next_lesson_id = lesson.get_next_lesson_id()
    
    # Print statements for debugging (optional)
    print('Lesson:', lesson)
    print('Previous Lesson ID:', previous_lesson_id)
    print('Next Lesson ID:', next_lesson_id)
    
    return render(request, 'lesson_detail.html', {
        'lesson': lesson,
        'subtopics': subtopics,
        'previous_lesson_id': previous_lesson_id,
        'next_lesson_id': next_lesson_id
    })

def level_selection(request):
    return render(request, 'level_selection.html')
