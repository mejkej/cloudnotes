from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.validators import MinLengthValidator, MaxLengthValidator

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}),
        validators =[
            MinLengthValidator(3),
            MaxLengthValidator(20)
        ],
    )
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), 
        validators=[
            MinLengthValidator(5),
            MaxLengthValidator(20),
        ],
)

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
    validators=[
        MinLengthValidator(5),
        MaxLengthValidator(20)
    ],
 )

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))