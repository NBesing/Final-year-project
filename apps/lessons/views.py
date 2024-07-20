from django.shortcuts import render, get_object_or_404
from .models import Lesson,Module
from django.contrib.auth.decorators import login_required

def lesson_list(request):
    lessons = Lesson.objects.all()
    return render(request, 'lessons/lesson_list.html', {'lessons': lessons})

def lesson_detail(request, module_id, lesson_id):
    print(f"Requested URL: /lessons/{module_id}/{lesson_id}/")

    lesson = get_object_or_404(Lesson, module_id=module_id, id=lesson_id)
    subtopics = lesson.content.get('subtopics', []) 
    modules = Module.objects.all()  

    
    # Get IDs of previous and next lessons
    previous_lesson_id = lesson.get_previous_lesson_id()
    next_lesson_id = lesson.get_next_lesson_id()

     # Get the user's first and last name
    user_first_name = request.session.get('user_first_name', '')
    user_last_name = request.session.get('user_last_name', '')
    
    # Print statements for debugging (optional)
    print('Lesson:', lesson)
    print('Previous Lesson ID:', previous_lesson_id)
    print('Next Lesson ID:', next_lesson_id)
    
    return render(request, 'lesson_detail.html', {
        'lesson': lesson,
        'modules': modules,
        'subtopics': subtopics,
        'previous_lesson_id': previous_lesson_id,
        'next_lesson_id': next_lesson_id
    })


@login_required
def level_selection(request):
    selected_module = Module.objects.first()  # Replace with your logic
    selected_lesson = Lesson.objects.filter(module=selected_module).first() if selected_module else None

    return render(request, 'level_selection.html', {
        'selected_module': selected_module,
        'selected_lesson': selected_lesson
    })