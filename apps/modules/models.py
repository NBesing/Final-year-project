from django.db import models
from apps.levels.models import Level

class Module(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    num_lessons = models.IntegerField()

    def __str__(self):
        return self.title

class ModuleExercise(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    description = models.TextField()
    exercises_content = models.TextField()
    num_attempts = models.IntegerField()
    num_questions = models.IntegerField()
    hints = models.TextField()
    def __str__(self):
        return self.description
