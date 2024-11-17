from django.urls import path
from . import views

urlpatterns = [
    path('', views.client_list, name='client_list'),  # List all clients
    path('add/', views.add_client, name='add_client'),  # Add a new client
    path('<int:client_id>/projects/', views.project_list, name='client_project_list'),  # Projects for a specific client
]
