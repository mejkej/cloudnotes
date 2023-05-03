from django.db import models
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomAuthenticationForm, CustomUserCreationForm


def entry_page(request):
    if request.method == 'POST':
        if 'signupform' in request.POST:
            upform = CustomUserCreationForm(request.POST)
            if upform.is_valid():
                upform.save()
                return redirect('main_app/main.html')
        elif 'signinform' in request.POST:
            inform = CustomAuthenticationForm(request, data=request.POST)
            if inform.is_valid():
                user = inform.get_user()
                login(request, user)
                return redirect('main_app/main.html')
    else:
        signinform = CustomAuthenticationForm()
        signupform = CustomUserCreationForm()
        context = {'signinform': signinform, 'signupform': signupform}
    return render(request, 'entry_app/entry.html', context)
