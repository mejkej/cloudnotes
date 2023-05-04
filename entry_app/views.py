from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from . forms import UserSignUpForm, UserSignInForm


def entry(request):
    if request.method == 'POST':
        if 'signup' in request.POST:
            signup_form = UserSignUpForm(request.POST)
            signin_form = UserSignInForm(request.POST)

            if signup_form.is_valid():
                user = signup_form.save()
                messages.success(request, 'Sign up successful!')
                return redirect('main.html')
        elif 'signin' in request.POST:
            signin_form = UserSignInForm(request.POST)
            signup_form = UserSignUpForm(request.POST)

            if signin_form.is_valid():
                username = signin_form.cleaned_data.get('username')
                password = signin_form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Welcome Back!')
                    return redirect('main.html')
                else:
                    messages.error(request, 'Username or password incorrect.')
            else:
                messages.error(request, 'Username or password incorrect.')
    else:
        signup_form = UserSignUpForm()
        signin_form = UserSignInForm()

    return render(request, 'entry.html', {'signup_form': signup_form, 'signin_form': signin_form})


