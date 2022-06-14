from django import forms
from users.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterForm(UserCreationForm):
    """Sign Up Form"""
    email = forms.EmailField(required=True, widget=forms.EmailInput())
    username = forms.CharField(required=True)
    birth_date = forms.DateField(widget=forms.DateInput())
    password1 = forms.CharField(required=True, widget=forms.PasswordInput())
    password2 = forms.CharField(required=True, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'birth_date', 'sex', 'password1', 'password2']


class LoginUserForm(AuthenticationForm):
    """Login Form"""
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True, widget=forms.EmailInput())
    password = forms.CharField(required=True, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']