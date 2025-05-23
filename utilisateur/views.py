
from django.shortcuts import render,redirect
from .forms import loginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.

def login_view(request):
    form = loginForm(request.POST or None)
    if form.is_valid():
       
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate( username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            form.add_error(None, "Nom d'utilisateur ou mot de passe incorrect.")
    return render(request, 'utilisateurs/login.html', {'form': form})
