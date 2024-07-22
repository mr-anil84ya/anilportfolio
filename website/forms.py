# myapp/forms.py
from django import forms
from django.core.exceptions import ValidationError
import re

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100,min_length=3, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Name',
        'class': 'form-control'
    }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'autocomplete': 'off',
        'type':'email',
        'class': 'form-control'
    }))
    phone = forms.CharField(max_length=15,min_length=10, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Phone',
        'class': 'form-control'
    }))
    subject = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Subject',
        'class': 'form-control'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Message',
        'rows': 3,
        'class': 'form-control'
    }), required=True)

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not re.match(r'^\+?1?\d{9,15}$', phone):
            raise ValidationError('Phone number must be entered in the format: "+999999999". Up to 15 digits allowed.')
        return phone
