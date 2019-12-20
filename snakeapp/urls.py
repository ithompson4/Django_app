from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('snakes/', views.snakes, name = 'snakes'),
    path('add-snake', views.add, name = 'add-snake'),    
    path('edit-snake/<int:id>', views.edit, name='edit-snake'),
    path('snake/<int:id>', views.show, name=''),
    path('delete-snake/<int:id>', views.delete, name='delete-snake'),
    path('home/', views.home, name='home'),
    path('registration/', views.appRegister, name='appRegister'),
    path('logout/',views.logout, name='logout'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('scientists/', views.scientists, name = 'scientists'),
    path('delete-scientist/<int:id>', views.delete_scientist, name='delete-scientist')
]
