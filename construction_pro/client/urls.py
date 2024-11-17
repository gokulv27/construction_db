from django.urls import path
from . import views

urlpatterns = [
#    path('', views.client_list, name='client_list'),
    path('add/', views.add_client, name='add_client'),
    path('client/<int:client_id>/projects/', views.project_list, name='project_list'),
]