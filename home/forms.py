from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
        labels = {
            'name': '',
            'email': '',
            'phone': '',
            'message': ''
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'feedback-input','placeholder': 'Nombre completo', 'label': ''}),
            'email': forms.EmailInput(attrs={'class': 'feedback-input', 'id': 'email-input', 'placeholder': 'Correo electrónico', 'label': ''}),
            'phone': forms.TextInput(attrs={'class': 'feedback-input', 'pattern': '[0-9]{3}[0-9]{3}[0-9]{4}','placeholder':'Número celular', 'label': ''}),
            'message': forms.Textarea(attrs={'class': 'feedback-input','placeholder': 'Mensaje', 'label': ''}),
        }
        label_suffix = ''
