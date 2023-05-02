from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import user_passes_test
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "password1", "password2")



# Create your views here.
@user_passes_test(lambda user: not user.is_authenticated, login_url='home', redirect_field_name=None)
def ENTRY_HTML(request):
    if request.method == 'POST':
        if 'signup' in request.POST:
            signupform = CustomUserCreationForm(request.POST)
            if signupform.is_valid():
                user = signupform.save()
                login(request, user)
                return redirect('home')  # Redirect to home page or any desired page
            else:
                signinform = AuthenticationForm()
        elif 'signin' in request.POST:
            signinform = AuthenticationForm(data=request.POST)
            if signinform.is_valid():
                user = signinform.get_user()
                login(request, user)
                return redirect('home')  # Redirect to home page or any desired page
            else:
                signupform = CustomUserCreationForm()
    else:
        form = UserCreationForm()
        form.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        form.fields['password1'].widget.attrs.update({'placeholder': 'Password'})
        form.fields['password2'].widget.attrs.update({'placeholder': 'Confirm Password'})

        login_form = AuthenticationForm()
        login_form.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        login_form.fields['password'].widget.attrs.update({'placeholder': 'Password'})

    context = {'signupform': signupform, 'signinform': signinform}
    return render(request, 'entry.html', context)

def HOMEPAGE(request):
    return render(request, 'home.html')