from django.urls import path
from . import views

urlpatterns = [
    path('', views.master_list, name='master_list'),
    path('api/items/', views.api_items, name='api_items'),
    path('api/items/<str:item_type>/', views.api_items, name='api_items_type'),
    path('api/items/<str:item_type>/<int:pk>/', views.api_items, name='api_items_detail'),
]