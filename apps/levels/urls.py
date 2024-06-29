from django.urls import path
from .views import level_list, level_detail

urlpatterns = [
    path('', level_list, name='level_list'),
    path('<int:pk>/', level_detail, name='level_detail'),
]
