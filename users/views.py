from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomAuthenticationForm
from django.contrib import messages


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomAuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('ecommerce:home')
            else:
                messages.error(request, "Usuario y/o contraseña inválido/a")
                return render(request, 'users/login.html')        
        else:
            context = {'form': CustomAuthenticationForm}
            return render(request, 'users/login.html', context)
    else:
        return redirect('ecommerce:home')


def logout_view(request):
    logout(request)
    return redirect('ecommerce:home')



'''

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm})
    else:
        try:
            if request.POST['password1'] == request.POST['password2']:
                print(request.POST)
                username = request.POST['username']
                password = request.POST['password1']
                user = User.objects.create_user(username=username, password=password)
                user.save()
                login(request, user)
                return redirect('tasks')
            else:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'submit_message': 'Passwords do not mach'
                })
        except IntegrityError:
            return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'submit_message': 'User already exist'
                })

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {'form': AuthenticationForm})
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'User or password incorrect'
                })
        else:
            login(request, user)
            return redirect('tasks')

@login_required
def signout(request):
    logout(request)
    return redirect('home')

'''