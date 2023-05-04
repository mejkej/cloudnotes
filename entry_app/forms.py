from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserSignUpForm(UserCreationForm):
    username = forms.CharField(min_length=3, max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Username', 'id': 'signup-username'}))
    password1 = forms.CharField(min_length=5, max_length=20, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'id': 'signup-password1'}))
    password2 = forms.CharField(min_length=5, max_length=20, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'id': 'signup-password2'}))

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("The username is not available.")
        return username

class UserSignInForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(min_length=5, max_length=20, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))