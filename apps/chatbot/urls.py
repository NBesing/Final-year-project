# chatbot/urls.py

# from django.urls import path
# from . import views

# app_name='chat'
# urlpatterns = [
#     path('chat/', views.chat_view, name='chat'),
    # Add other paths as needed
# ]

from django.urls import path
from .views import exercise_view

urlpatterns = [
    path('generate/', exercise_view, name='generate_exercise'),
]
