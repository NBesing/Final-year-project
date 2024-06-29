from django.urls import path
from .views import progress_list, grade_list

urlpatterns = [
    path('progress/', progress_list, name='progress_list'),
    path('grades/', grade_list, name='grade_list'),
]
