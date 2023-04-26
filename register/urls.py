from django.urls import path
from . import views 

urlpatterns = [
    path('', views._list, name='employee'),
    path('form/', views._form, name='employee_form'),
    path('positions/', views._positions, name='employee_positions'),
    path('del/<int:pk>/', views._del, name='employee_del'),
    path('edit/<int:pk>/', views._edit, name='employee_edit'),
]
