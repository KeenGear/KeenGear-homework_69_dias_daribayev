from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add),
    path('substract/', views.subtract),
]
