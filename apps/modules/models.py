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
    title = models.TextField()
    content = models.TextField()
    number_of_attempts = models.IntegerField()
    number_of_hints = models.IntegerField()
    hints = models.JSONField(default=list) # Use JSONField for MySQL

    def __str__(self):
        return self.title
