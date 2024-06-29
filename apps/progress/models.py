from django.db import models
from apps.accounts.models import User
from apps.modules.models import Module
from apps.lessons.models import Lesson
from apps.assessment.models import Assessment

class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user} - {self.module} - {self.lesson} - {self.status}"

class Grade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    grade = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user} - {self.module} - {self.assessment} - {self.grade}"
