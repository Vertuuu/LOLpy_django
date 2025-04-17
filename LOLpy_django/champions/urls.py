from django.urls import path
from . import views
urlpatterns = [
    path('champions/', views.champions, name='champions')
]