from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:plane_id>/', views.details, name='plane')
]
