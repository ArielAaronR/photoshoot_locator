from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('dashboard', views.dashboard),
    path('register', views.register),
    path('login', views.login),
    path('new', views.new),
    path('new_process', views.new_process),
    path('spot/<int:id>/delete', views.delete),
    path('logout', views.logout),
]
