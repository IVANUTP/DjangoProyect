"""
URL configuration for Miapp project.

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
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path("signup/",views.signup, name='signup'),
    path("tasks/",views.tasks, name='tasks'),
    path("tasks_complete/",views.tasks_complete, name='tasks_complete'),
    path("tasks/create",views.create_tasks, name='create_tasks'),
    path("tasks/<int:tasks_id>",views.tasks_deta, name='tasks_deta'),
    path("tasks/<int:task_id>/completo", views.complete_taks, name='complete_task'),
    path("tasks/<int:task_id>/delete", views.delete, name='eliminar'),
    path("logout/",views.signout, name='logout'),
    path("signing/",views.signin, name='signing')
]
