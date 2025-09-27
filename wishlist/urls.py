from django.urls import path
from . import views

app_name = 'wishlist'

urlpatterns = [
    path('', views.view_wishlist, name='view_wishlist'),
    path('mark/<int:item_id>/', views.mark_purchased, name='mark_purchased'),
]
