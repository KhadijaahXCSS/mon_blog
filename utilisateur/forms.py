from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class loginForm(forms.Form):
    username = forms.CharField(
        label='Nom d\'utilisateur',
        widget=forms.TextInput(attrs={
            "class": "form-control",
        }),
        max_length=100
    )
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput
                               (attrs={
            "class": "form-control",
        }))
    
class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label='Nom d\'utilisateur',
        widget=forms.TextInput(attrs={
            "class": "form-control",
        }),
        max_length=100
    )
    email = forms.EmailField(
        label='Adresse e-mail',
        widget=forms.EmailInput(attrs={
            "class": "form-control",
        }),
        max_length=254
    )
    password1 = forms.CharField(label='Mot de passe', widget=forms.PasswordInput
                               (attrs={
            "class": "form-control",
        }))
    password2 = forms.CharField(label='Confirmer le mot de passe', widget=forms.PasswordInput
                                       (attrs={
            "class": "form-control",
        }))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')