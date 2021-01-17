from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='photomatch-index'),
    path('landing/', views.landing, name='photomatch-landing'),
]