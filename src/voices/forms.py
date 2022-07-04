from django import forms
from voices.models import Record


class CreateRecord(forms.Form):
    record_text = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Record text'}))
