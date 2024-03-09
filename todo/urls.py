
from django.urls import path
from todo import views

urlpatterns = [
   path('', views.home, name='home-page'),
   path('register/', views.register, name='register-page'),
   path('todos/', views.task, name='todo-page'),

   path('create-task/', views.create_task, name='create-task-page'),
   path('delete-task/<int:pk>/', views.delete_task, name='delete-task-page'),

]


htmx_patterns = [
    path('check_available/', views.check_user_availability, name='check-available-page'),
]

urlpatterns += htmx_patterns
