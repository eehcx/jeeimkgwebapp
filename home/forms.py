from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput( attrs={'class': 'feedback-input','placeholder': 'Nombre completo'}),
            'email': forms.EmailInput(attrs={'class': 'feedback-input', 'id': 'email-input', 'placeholder': 'Correo electrónico'}),
            'phone': forms.TextInput(attrs={'class': 'feedback-input', 'pattern': '[0-9]{3}[0-9]{3}[0-9]{4}','placeholder':'Número celular'}),
            'message': forms.Textarea(attrs={'class': 'feedback-input','placeholder': 'Mensaje'}),
        }




"""
    def save(self, commit=True):
        instance = super(ContactForm, self).save(commit=False)
        if commit:
            instance.save()
            instance.save_to_firestore()
        return instance
"""
