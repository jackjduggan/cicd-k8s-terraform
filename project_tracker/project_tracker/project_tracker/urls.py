from django.contrib import admin
from django.urls import path

from projects import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),                                              # localhost:8080/
    path('projects/<int:project_id>', views.project_detail, name='project_detail')  # localhost:8080/projects/1
]
