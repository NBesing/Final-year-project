from django.db import models
from apps.lessons.models import LessonExercise
from apps.modules.models import ModuleExercise
from apps.accounts.models import User

class Assessment(models.Model):
    description = models.TextField()
    assessment_content = models.TextField()

    def __str__(self):
        return self.description

class AssessmentQuestion(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    question = models.TextField()
    question_type = models.CharField(max_length=50)

    def __str__(self):
        return self.question

class Answer(models.Model):
    lesson_exercise = models.ForeignKey(LessonExercise, on_delete=models.CASCADE, null=True, blank=True)
    module_exercise = models.ForeignKey(ModuleExercise, on_delete=models.CASCADE, null=True, blank=True)
    assessment_question = models.ForeignKey(AssessmentQuestion, on_delete=models.CASCADE)
    answer = models.TextField()
    is_correct = models.BooleanField()

    def __str__(self):
        return self.answer

class StudentResponse(models.Model):
    lesson_exercise = models.ForeignKey(LessonExercise, on_delete=models.CASCADE, null=True, blank=True)
    module_exercise = models.ForeignKey(ModuleExercise, on_delete=models.CASCADE, null=True, blank=True)
    assessment_question = models.ForeignKey(AssessmentQuestion, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    response = models.TextField()

    def __str__(self):
        return self.response
