from django import forms
from users.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterForm(UserCreationForm):
    """Sign Up Form"""
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    birth_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'birth_date', 'sex', 'password1', 'password2']


class LoginUserForm(AuthenticationForm):
    """Login Form"""
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class UpdateUserForm(forms.ModelForm):
    """Update User"""
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    avatar_image = forms.ImageField(widget=forms.FileInput())

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'last_name', 'birth_date', 'avatar_image']



