"""
URL configuration for resume_upload project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from resume import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.function,name="home"),
    path('data/', views.resumedata,name="resumedata"),  
    path('show/', views.show_resume,name="show_resume"),
     path('candidate/<int:candidate_id>/', views.candidate_detail, name='candidate_detail'),
    path('resume/delete/<int:candi_id>/', views.delete_data,name="delete_data"),
    path('job/edit/<int:candidate_id>/', views.update_data,name="update_data"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)