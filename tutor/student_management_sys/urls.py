from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name = 'index'),
    path('read/',views.read,name = 'read'),
   path('update/<int:id>/', views.update, name='update'),
   path('delete/<int:id>/', views.delete, name='delete'),
   
]
  