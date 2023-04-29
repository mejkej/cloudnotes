from django.shortcuts import render

# Create your views here.
def ENTRY_HTML(request):
    return render(request, 'entry.html')