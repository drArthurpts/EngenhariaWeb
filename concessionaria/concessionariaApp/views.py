from django.shortcuts import render,redirect
from .admin import CustomUserCreationForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import views as auth_views

def index(request):
    return render(request, 'concessionaria/index.html')


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