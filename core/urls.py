from django.urls import path
from . import views

urlpatterns = [
    path('', views.todos, name='index'),
    path('create-todo/', views.create_todo, name='create-todo'),
    path('update-todo/<int:id>/', views.update_todo, name='update-todo'),
    path('delete-todo/<int:id>/', views.delete_todo, name='delete-todo'),
]
