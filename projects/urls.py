from django.urls import path

from .views import projects_list, project_detail, createProject, updateProject, deleteProject


urlpatterns = [
    path('', projects_list, name='projects_list'),
    path('project/<str:pk>/', project_detail, name='project_detail'),

    path('create_project', createProject, name='create_project'),
    path('update_project/<str:pk>/', updateProject, name='update_project'),
    path('delete/<str:pk>/', deleteProject, name='delete_project'),
]