from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
@login_required
def MAIN_APP(request):
    return render(request, 'main.html')

def LOGOUT_VIEW(request):
    logout(request)
    return redirect('entry.html')
