from django.db import models
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomAuthenticationForm, CustomUserCreationForm


def ENTRY_APP(request):
    if request.method == 'POST':
        if 'signupform' in request.POST:
            upform = CustomUserCreationForm(request.POST)
            if upform.is_valid():
                upform.save()
                return redirect('main')
        elif 'signinform' in request.POST:
            inform = CustomAuthenticationForm(request, data=request.POST)
            if inform.is_valid():
                user = inform.get_user()
                login(request, user)
                return redirect('main')
    else:
        signinform = CustomAuthenticationForm()
        signupform = CustomUserCreationForm()
        context = {'signinform': signinform, 'signupform': signupform}
        return render(request, 'entry.html', context)
