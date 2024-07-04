from django.db import models
from apps.modules.models import Module

class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.JSONField() 

    def __str__(self):
        return self.title

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
