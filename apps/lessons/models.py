from django.db import models
from apps.modules.models import Module

class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.JSONField() 

    def __str__(self):
        return self.title
    
    def get_previous_lesson_id(self):
        # Implement logic to get ID of previous lesson
        previous_lesson = Lesson.objects.filter(id__lt=self.id).order_by('-id').first()
        if previous_lesson:
            return previous_lesson.id
        return None

    def get_next_lesson_id(self):
        # Implement logic to get ID of next lesson
        next_lesson = Lesson.objects.filter(id__gt=self.id).order_by('id').first()
        if next_lesson:
            return next_lesson.id
        return None

class Example(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    description = models.TextField()
    example_content = models.TextField()

    def __str__(self):
        return self.description

class LessonExercise(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    description = models.TextField()
    exercise_content = models.TextField()

    def __str__(self):
        return self.description
