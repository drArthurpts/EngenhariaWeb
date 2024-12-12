from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página inicial
    path('register', views.register, name='register'),  # Registro de usuários
    path('register_car', views.register_car_page, name='register_car_page'),  # Página de cadastro
    path('register_car/submit', views.register_car, name='register_car'),   # Registro de carros
]
