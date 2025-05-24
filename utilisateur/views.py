
from django.shortcuts import render,redirect
from .forms import loginForm, RegisterForm
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

def register_view(request):
    if request.method == 'POST':
        
        form= RegisterForm(request.POST )
        if form.is_valid():
            form.save()
        
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            
        # email = form.cleaned_data.get('email')
            #confirm_password = form.cleaned_data.get('confirm_password')
            user = authenticate(username=username, password1=raw_password)
            return redirect('login')
    else:
        form = RegisterForm()
    
    
   
    return render(request, 'utilisateurs/register.html', {'form': form})



