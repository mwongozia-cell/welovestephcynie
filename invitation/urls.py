from django.urls import path
from . import views

app_name = 'invitation'

urlpatterns = [
    path('', views.home, name='home'),
    path('rsvp/attending/', views.rsvp_attending, name='rsvp_attending'),
    path('rsvp/celebrating/', views.rsvp_celebrating, name='rsvp_celebrating'),
    path('rsvp/regrets/', views.rsvp_regrets, name='rsvp_regrets'),
    path('contribute/', views.contribute, name='contribute'),
    path('login/', views.login_view, name='login'),
]
