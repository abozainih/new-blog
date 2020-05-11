from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login , logout
from django.shortcuts import redirect





def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user) 
            
            return redirect('posts')

    else :
        form = UserCreationForm()
    
    return render(request,'accounts/register.html',{'form':form})



def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('posts')  
    else :
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})


def log_out(request):
    logout(request)
    return redirect('login')
