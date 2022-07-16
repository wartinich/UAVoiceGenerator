from django import forms
from apps.voices.models import Record


class CreateRecord(forms.Form):
    record_text = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Привіт!',
            'class': 'record_text'
        }))
