from django import forms
from django.contrib.auth.forms import UserCreationForm
from firebase_admin import credentials, auth, firestore, exceptions

"""| Esta función me registra mis usuarios y me los muestra en mi Sign Up |"""
class FirebaseSignupForm(forms.Form):
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'id': 'email-input', 'class': 'feedback-input', 'placeholder':'Correo Electronico'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'feedback-input', 'placeholder':'Contraseña'}))
    password_confirm = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'feedback-input', 'placeholder':'Confirmar Contraseña'}))

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return cleaned_data

    def signup(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        try:
            # Crea un usuario en Authentication
            user = auth.create_user(
                email=email,
                password=password
            )
        except exceptions.FirebaseError as e:
            # Maneja el error aquí
            pass




