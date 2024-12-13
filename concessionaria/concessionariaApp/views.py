from django.shortcuts import render,redirect
from .admin import CustomUserCreationForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import views as auth_views
from .models import Car
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .forms import CarForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Car


@login_required
def my_cars(request):
    cars = Car.objects.filter(user=request.user)  # Filtra apenas os carros do usuário logado
    return render(request, 'concessionaria/my_cars.html', {'cars': cars})


@login_required
def edit_car(request, car_id):
    car = get_object_or_404(Car, id=car_id, user=request.user)
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('my_cars')
    else:
        form = CarForm(instance=car)

    # Atualize o caminho para refletir a localização correta do template
    return render(request, 'concessionaria/edit_car.html', {'form': form})


@login_required
def delete_car(request, car_id):
    car = get_object_or_404(Car, id=car_id, user=request.user)
    if request.method == 'POST':
        car.delete()
        return redirect('my_cars')

    # Atualize o caminho para refletir a localização correta do template
    return render(request, 'concessionaria/delete_car.html', {'car': car})

def index(request):
    cars = Car.objects.all()  # Obtém todos os carros do banco de dados
    return render(request, 'concessionaria/index.html', {'cars': cars})


def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Bem-vindo, {user.username}!")
            return redirect('index')
        else:
            messages.error(request, "Usuário ou senha inválidos.")
    
    # Alterar o caminho para 'registration/login.html'
    return render(request, 'registration/login.html')


def custom_logout(request):
    logout(request)
    messages.success(request, 'Você saiu com sucesso!')
    return redirect('login')

def register(request):
    if request.method == "POST":
        # Preenche o formulário com os dados enviados via POST
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Salva o usuário no banco de dados
            user = form.save()
            
            # Mensagem de sucesso
            messages.success(request, 'Registrado com sucesso! Agora você pode fazer login.')
            
            # Redireciona para a página de login
            return redirect('login')
        else:
            # Mensagem de erro em caso de falha no formulário
            messages.error(request, 'Erro no registro. Verifique os dados e tente novamente.')
    else:
        # Cria uma instância vazia do formulário para GET requests
        form = CustomUserCreationForm()
    
    # Renderiza o formulário na página
    return render(request, "registration/register.html", {"form": form})



def register_car_page(request):
    return render(request, 'concessionaria/register_car.html')

@login_required
def register_car(request):
    if request.method == 'POST':
        brand = request.POST.get('brand')
        model = request.POST.get('model')
        year = request.POST.get('year')
        price = request.POST.get('price')
        image = request.FILES.get('image')

        # Salvar no banco, associando ao usuário autenticado
        car = Car(
            brand=brand,
            model=model,
            year=year,
            price=price,
            image=image,
            user=request.user  # Associa o carro ao usuário autenticado
        )
        car.save()

        return redirect('index')  # Redirecionar após cadastro

    return render(request, 'register_car.html') # Redirecionar após cadastro

def search_cars(request):
    model_query = request.GET.get('model', '').strip()
    if model_query:
        cars = Car.objects.filter(model__icontains=model_query)
    else:
        cars = Car.objects.all()
    return render(request, 'concessionaria/search_results.html', {'cars': cars})

def car_details(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'concessionaria/car_details.html', {'car': car})


def confirm_purchase(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        # Processamento da compra
        buyer_name = request.POST['buyer_name']
        buyer_email = request.POST['buyer_email']
        buyer_phone = request.POST['buyer_phone']
        
        # Lógica de compra (salvar no banco de dados ou enviar email)
        
        # Redireciona após compra bem-sucedida
        return redirect('purchase_success') 