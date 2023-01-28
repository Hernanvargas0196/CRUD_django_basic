"""djangocrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('signUp/', views.signup, name="signUp"),
    path('tasks/', views.tasks, name="tasks"),
    path('signOff', views.signOff, name="signOff" ),
    path('signIn/', views.signIn, name="signIn"),
    path('create_task/', views.create_task, name="create_task"),
    path('tasks/<int:task_id>', views.task_detail, name="task_detail"),
    path('tasks/<int:task_id>/delete', views.delete_task, name="delete_task")
]