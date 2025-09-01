from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('add/', views.project_create, name='project_create'),
    path('<int:pk>/edit/', views.project_edit, name='project_edit'),
    path('<int:pk>/delete/', views.project_delete, name='project_delete'),
]
