from django.urls import path # type: ignore
from . import views

urlpatterns = [
    # path('', views.home, name='home'),  # Home page
    path('project/', views.project_list, name='project_list'),  # Project list
    path('project/<int:pk>/', views.project_detail, name='project_detail'),  # Project detail
]
