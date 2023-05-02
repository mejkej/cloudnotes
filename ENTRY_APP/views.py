from django.db import models
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def ENTRY_APP(request):
    if request.method == 'POST':
        if 'signupform' in request.POST:
            upform = UserCreationForm(request.POST)
            if upform.is_valid():
                upform.save()
                return redirect('entry')
        elif 'signinform' in request.POST:
            inform = AuthenticationForm(data=request.POST)
            if inform.is_valid():
                user = inform.get_user()
                login(request, user)
                return redirect('home')
    else:
        signinform = AuthenticationForm()
        signupform = UserCreationForm()
        context = {'signinform': signinform, 'signupform': signupform}
        return render(request, 'entry.html', context)
    return render(request, 'entry.html')