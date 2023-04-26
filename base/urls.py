from django.urls import path
from . import views
urlpatterns = [
    path('', views._home, name='home')
]
