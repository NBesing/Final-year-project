from django.urls import path
from .views import assessment_list, assessment_detail

urlpatterns = [
    path('', assessment_list, name='assessment_list'),
    path('<int:pk>/', assessment_detail, name='assessment_detail'),
]
