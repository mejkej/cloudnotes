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
                message.success(request, 'Signed in successfully')
                return redirect('main.html')
            else:
                messages.error(request, 'Username or password incorrect.')
    else:
        form = SignInForm()

    context = {'signinform': form,}

    return render(request, 'signin.html', context)


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Signed up succesfully, Lets sign in!')
            return redirect('signin.html')
    else:
        form = SignUpForm()

    context = {'signupform': form,}

    return render(request, 'signup.html', context)

            


