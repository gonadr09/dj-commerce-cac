from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, UsernameField
from django.utils.translation import gettext_lazy as _
from .models import CustomUser


# Formulario basado en clases (AuthenticationForm hereda de forms.Form) -> class AuthenticationForm(forms.Form)
class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={
            'autofocus': True,
            'class': 'form-control',
            'placeholder': ' ',
        }),
        required=True
    )

    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'current-password',
            'class': 'form-control',
            'placeholder': ' ',
            }),
        required=True
    )

# Formulario asociado a un modelo (UserCreationForm hereda de forms.ModelForm) -> class UserCreationForm(forms.ModelForm)
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'dni', 'phone', 'address', 'city', 'state')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = ' '


# Formulario asociado a un modelo (UserChangeForm hereda de forms.ModelForm) -> class UserChangeForm(forms.ModelForm)
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'dni', 'phone', 'address', 'city', 'state')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = ' '
            