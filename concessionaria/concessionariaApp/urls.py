from django.urls import path
from . import views  # Certifique-se de importar as views

urlpatterns = [
    path('', views.index, name='index'),  # Página inicial
    path('register', views.register, name='register'),  # Registro de usuários
    path('register_car', views.register_car_page, name='register_car_page'),  # Página de cadastro
    path('register_car/submit', views.register_car, name='register_car'),   # Registro de carros
    
    # Login e Logout
    path('login/', views.custom_login, name='login'),  # Página de login
    path('logout/', views.custom_logout, name='logout'),  # Logout

    path('my_cars/', views.my_cars, name='my_cars'),
    path('my_cars/edit/<int:car_id>/', views.edit_car, name='edit_car'),
    path('my_cars/delete/<int:car_id>/', views.delete_car, name='delete_car'),

    path('search/', views.search_cars, name='car_search'),

    path('car/<int:car_id>/', views.car_details, name='car_details'),

    path('car/<int:car_id>/buy/', views.confirm_purchase, name='confirm_purchase'),

]
