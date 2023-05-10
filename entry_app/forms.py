from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    username = forms.CharField(
    max_length=20,
    min_length=3,
    widget=forms.TextInput(attrs={'placeholder': 'Username'}))

    password1 = forms.CharField(
    max_length=20,
    min_length=5,
    widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    password2 = forms.CharField(
    max_length=20,
    min_length=5,
    widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username not available.")
        return username


class SignInForm(AuthenticationForm):
    username = forms.CharField(
    max_length=20,
    min_length=3,
    widget=forms.TextInput(attrs={'placeholder': 'Username'}))

    password = forms.CharField(
        max_length=20,
        min_length=5,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )
