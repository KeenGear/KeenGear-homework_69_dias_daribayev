from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add),
    path('subtract/', views.subtract),
    path('multiply/', views.multiply),
    path('divide/', views.divide),
]
