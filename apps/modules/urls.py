# urls.py in apps.modules

from django.urls import path
from . import views

app_name = 'modules'

urlpatterns = [
    path('module_list/', views.module_list, name='module_list'),
    path('modules/exercise/<int:module_id>/', views.module_exercise, name='module_exercise'),
    path('api/exercises/<int:exercise_id>/', views.exercise_detail_view, name='exercise_detail'),
    path('exercise_list/', views.exercise_list, name='exercise_list'),
]
