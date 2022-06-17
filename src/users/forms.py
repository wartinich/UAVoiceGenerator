from django import forms
from users.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib import messages


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
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class UpdateUserForm(forms.ModelForm):
    """Update User"""
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    username = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    birth_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    avatar_image = forms.ImageField(required=False, widget=forms.FileInput())

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'last_name', 'birth_date', 'sex', 'avatar_image']


class CustomChangePasswordForm(PasswordChangeForm):
    """Customize PasswordChangeForm"""
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Old password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'New password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm new password'}))


