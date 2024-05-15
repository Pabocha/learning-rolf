from django import forms
from .models import Contacts


class ContactForm(forms.ModelForm):
    class Meta:

        model = Contacts
        fields = '__all__'

        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Votre nom'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Votre email'}),
            'sujet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'sujet'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'message'}),
        }
