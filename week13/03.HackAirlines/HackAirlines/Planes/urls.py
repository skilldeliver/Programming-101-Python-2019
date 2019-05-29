from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:plane_id>/', views.details, name='plane'),
    path('flights/', views.flights),
    path('flights/create/', views.create_flight)
]
