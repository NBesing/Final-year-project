# urls.py in apps.modules

from django.urls import path
from . import views

urlpatterns = [
    path('module_list/', views.module_list, name='module_list'),
    path('module_exercise/', views.module_exercise, name='module_exercise'),
    path('exercise_list/', views.exercise_list, name='exercise_list'),
]
