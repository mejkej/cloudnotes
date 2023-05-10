from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import SignUpForm, SignInForm


def signin_view(request):
    return render(request, 'signin.html')

