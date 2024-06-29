from django.urls import path
from . import views 

urlpatterns = [
    path('', views.lesson_list, name='lesson_list'),
    path('lesson_detail/<int:pk>/', views.lesson_detail, name='lesson_detail'),
    path('level_selection/', views.level_selection, name='level_selection'),

]
