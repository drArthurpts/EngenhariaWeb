from django.shortcuts import render,redirect
from .admin import CustomUserCreationForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import views as auth_views
from .models import Car

def index(request):
    cars = Car.objects.all()  # Obtém todos os carros do banco de dados
    return render(request, 'concessionaria/index.html', {'cars': cars})


def register(request):
        form = CustomUserCreationForm()
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST)
    
            if form.is_valid():
                user = form.save(commit=False)
                user.is_valid = False
                user.save()
                messages.success(request, 'Registrado. Agora faça o login para começar!')
                return redirect('index')

            else:
                print('invalid registration details')
                
        return render(request, "registration/register.html",{"form": form})



def register_car_page(request):
    return render(request, 'concessionaria/register_car.html')

def register_car(request):
    if request.method == 'POST':
        brand = request.POST.get('brand')
        model = request.POST.get('model')
        year = request.POST.get('year')
        price = request.POST.get('price')
        image = request.FILES.get('image')

        # Salvar no banco
        car = Car(brand=brand, model=model, year=year, price=price, image=image)
        car.save()

        return redirect('index')  # Redirecionar após cadastro