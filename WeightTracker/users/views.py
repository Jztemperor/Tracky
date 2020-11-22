from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user =  form.save()
            messages.success(request, f'Your account has been created!')
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password = form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('landing-home')
    else:
        form = UserRegisterForm()
        
    return render(request, 'users/register.html',{'form':form})

       
  
        





    


