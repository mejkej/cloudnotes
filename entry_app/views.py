from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserSignUpForm, UserSignInForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def entry_view(request):
    signup_form = UserSignUpForm(request.POST if 'signup' in request.POST else None)
    signin_form = UserSignInForm(request.POST if 'signin' in request.POST else None)

    if request.method == 'POST':
        if 'signup' in request.POST:
            if signup_form.is_valid():
                user = signup_form.save()
                messages.success(request, 'Signed up successfully!')
                return redirect('entry_app:entry')
        elif 'signin' in request.POST:
            if signin_form.is_valid():
                username = signin_form.cleaned_data.get('username')
                password = signin_form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Welcome Back!')
                    return redirect('main_app:main')
                else:
                    messages.error(request, 'Username or password incorrect.')
            else:
                messages.error(request, 'Username or password incorrect.')

    return render(request, 'entry_app/entry.html', {'signup_form': signup_form, 'signin_form': signin_form})


