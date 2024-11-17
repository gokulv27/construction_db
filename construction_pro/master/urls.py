from django.urls import path
from . import views

urlpatterns = [
    path('', views.master_list, name='master_list'),  # Master list page
    path('api/items/', views.api_items, name='api_items'),  # API to list all items
    path('api/items/<str:item_type>/', views.api_items, name='api_items_type'),  # Filter items by type
    path('api/items/<str:item_type>/<int:pk>/', views.api_items, name='api_items_detail'),  # Item details by type and ID
]
