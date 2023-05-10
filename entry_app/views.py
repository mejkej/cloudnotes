from django.shortcuts import render, redirect


def signin_view(request):
    return render(request, 'entry_app/signin.html')

