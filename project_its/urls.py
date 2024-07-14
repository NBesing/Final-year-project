from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/', include('apps.accounts.urls')),
    path('levels/', include('apps.levels.urls')),
    path('modules/', include('apps.modules.urls')),
    path('lessons/', include('apps.lessons.urls')),
    path('chatbot/', include('apps.chatbot.urls')),
    path('assessment/', include('apps.assessment.urls')),
    # path('progress/', include('apps.progress.urls')),
]




# """
# URL configuration for project_its project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static



# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('authentication/', include('authentication.urls')),
#     path('quiz/', include('quiz.urls')),
#     path('course/', include('course.urls')),
#     path('chat/', include('chat.urls')),
#     path('ai/', include('ai.urls')),
#     path('example/', include('example.urls')),
#     path("", include('myproject.urls'))
# ]

# # if settings.DEBUG:
# #     urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# #     urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

