from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomAuthenticationForm, CustomUserCreationForm, CustomUserChangeForm


def login_view(request):
    if not request.user.is_authenticated:  # ToDo: averiguar el decorador is_authenticated
        if request.method == 'POST':
            form = CustomAuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('ecommerce:home')
            else:
                return render(request, 'users/login.html', {'form': form})
        else:
            return render(request, 'users/login.html', {'form': CustomAuthenticationForm})
    else:
        return redirect('ecommerce:home')
    

def logout_view(request):
    logout(request)
    return redirect('ecommerce:home')


def signup_view(request):
    if not request.user.is_authenticated:  # ToDo: averiguar el decorador is_authenticated
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, '¡Tu cuenta ha sido creada correctamente! Ya podés iniciar sesión.')
                return redirect('users:login')
            else:
                return render(request, 'users/signup.html', {'form': form})
        else:
            return render(request, 'users/signup.html', {'form': CustomUserCreationForm})
    else:
        return redirect('ecommerce:home')
    

@login_required
def profile_view(request):
    user = request.user
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            print(user.username)
            print(form.cleaned_data['username'])
            if form.cleaned_data['username'] == user.username:
                form.save()
                messages.success(request, 'Perfil actualizado con éxito', extra_tags='success')
                return redirect('users:profile')
            else:
                messages.error(request, 'Error al guardar', extra_tags='danger')
                return render(request, 'users/profile.html', {'form': form})
        else:
            return render(request, 'users/profile.html', {'form': form})
    else:
        form = CustomUserChangeForm(instance=user)
        return render(request, 'users/profile.html', {'form': form})
