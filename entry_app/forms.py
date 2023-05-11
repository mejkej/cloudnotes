from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator
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
    validators=[MinLengthValidator(5), MaxLengthValidator(20)],
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

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 5 or len(password1) > 20:
            raise forms.ValidationError("Password must be between 5 and 20 characters.")
        return password1


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
