# urls.py in apps.lessons

from django.urls import path
from . import views

app_name = 'lessons'

urlpatterns = [
    path('', views.lesson_list, name='lesson_list'),
    path('module/<int:module_id>/lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('level_selection/', views.level_selection, name='level_selection'),
]
