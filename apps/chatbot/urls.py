# chatbot/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chat_view, name='chat'),
    # Add other paths as needed
]
