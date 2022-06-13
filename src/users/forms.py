from django import forms
from users.models import User


class LoginForm(forms.ModelForm):
    password1 = forms.CharField(required=True, widget=forms.PasswordInput())
    password2 = forms.CharField(required=True, widget=forms.PasswordInput())


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']