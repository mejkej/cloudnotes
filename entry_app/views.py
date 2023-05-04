from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from . forms import UserSignUpForm, UserSignInForm

def not_authenticated(user):
    return not user.is_authenticated

@user_passes_test(not_authenticated, login_url='user_signin')
def user_signup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Sign up successful!')
            return redirect('user_signin')
    else:
        form = UserSignUpForm()
    return render(request, 'entry.html', {'signup_form': form})

def user_signin(request):
    if request.method == 'POST':
        form = UserSignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Welcome Back!')
                return redirect('main_page')
            else:
                messages.error(request, 'Username or password incorrect.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = UserSignInForm()
    return render(request, 'entry.html', {'signin_form': form})

def user_logout(request):
    logout(request)
    messages.success(request, 'Signed out succesfully!')
    return redirect('user_signin')
