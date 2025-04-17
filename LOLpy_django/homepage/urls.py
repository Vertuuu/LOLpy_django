from django.urls import path
from champions import views as champions_views
from . import views

urlpatterns = [
    path('champions/', champions_views.champions, name='champions'),
    path('home/', views.homepage, name='homepage'),
    path('', views.homepage, name='homepage')
]