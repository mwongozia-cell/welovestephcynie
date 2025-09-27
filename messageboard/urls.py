from django.urls import path
from . import views

app_name = 'messageboard'

urlpatterns = [
    path('shoutouts/', views.shoutout_board, name='shoutout_board'),
    path('shoutout/', views.shoutout, name='shoutout'),
]
