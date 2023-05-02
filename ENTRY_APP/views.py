from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

def MAIN_APP(request):
    return render(request, 'main.html')

def ENTRY_APP(request):
    if request.method == 'POST':
        if 'signupform' in request.POST:
            signupform = UserCreationForm(request.POST)
            if signupform.is_valid():
                user = signupform.save()
                login(request, user)
                return redirect('main')
        elif 'signinform' in request.POST:
            signinform = AuthenticationForm(data=request.POST)
            if signinform.is_valid():
                user = signinform.get_user()
                login(request, user)
                return redirect('main')
    else:
        signupform = UserCreationForm()
        signinform = AuthenticationForm()
        return render(request, 'entry.html', {'signupform': signupform, 'signinform': signinform})
