
from django.urls import path
from todo import views

urlpatterns = [
   path('', views.home, name='home-page'),
   path('register/', views.register, name='register-page'),
   
]


htmx_patterns = [
    path('check_available/', views.check_user_availability, name='check-available-page'),
]

urlpatterns += htmx_patterns
