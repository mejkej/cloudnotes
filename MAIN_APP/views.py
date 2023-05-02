from django.contrib.auth import logout
from django.shortcuts import render, redirect

def MAIN_APP(request):
    if request.method == 'POST' and 'logout' in request.POST:
        logout(request)
        return redirect('entry')
    else:
        return render(request, 'main.html')