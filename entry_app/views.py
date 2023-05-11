from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import SignUpForm, SignInForm


def signin_view(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Signed in successfully')
                return redirect('main')
            else:
                messages.error(request, 'Username or password incorrect.')
    else:
        form = SignInForm()

    context = {'signinform': form,}

    return render(request, 'entry_app/signin.html', context)


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Signed up successfully. Lets Sign in!')
            return redirect('signin')

        else:
            messages.error(request, 'Username not available.')

    else:
        form = SignUpForm()

    context = {'signupform': form,}

    return render(request, 'entry_app/signup.html', context)
