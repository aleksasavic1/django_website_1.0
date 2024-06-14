from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('fruits/', views.fruits, name='fruits'),
    path('training/', views.training, name='training'),
    path('about_me/', views.about_me, name='about_me'),
]
