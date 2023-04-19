from django import forms
#from .models import Client
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from datetime import datetime

class ClientForm(forms.Form):
    name = forms.CharField(label="", max_length=255, widget=forms.TextInput(attrs={'class': 'feedback-input', 'placeholder': 'Nombre Empresa'}))
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'feedback-input', 'id': 'email-input', 'placeholder':'Correo Electronico'}))
    phoneNumber = forms.CharField(label="Número celular", max_length=10, widget=forms.TextInput(attrs={'class': 'feedback-input', 'pattern': r'^\d{3}\d{3}\d{4}$', 'placeholder': 'Número celular'}), help_text='El número de teléfono debe tener 10 dígitos sin espacios ni guiones')
    sector = forms.ChoiceField(label="Selecciona tu Giro", choices=[
        ('', 'Selecciona tu Giro'),
        ('industrial', 'Industrial'),
        ('comercial', 'Comercial'),
        ('servicios', 'Servicios')
    ], widget=forms.Select(attrs={'class': 'feedback-input'}), required=True)
    service = forms.ChoiceField(label="Selecciona un servicio", choices=[
        ('', 'Selecciona un servicio'),
        ('plan-social-media', 'Plan Social Media'),
        ('grilla-mensual', 'Grilla contenidos (Mensual)'),
        ('grilla-semanal', 'Grilla contenidos (Semanal)'),
        ('pack-videos-semanal', 'Pack de videos (5 semanal)'),
        ('pack-videos-mensual', 'Pack de videos (20 mensual)'),
        ('pack-imagenes-semanal', 'Pack de imágenes/ post (10 semanal)'),
        ('pack-imagenes-mensual', 'Pack de imágenes/ post (30 mensual)')
    ], widget=forms.Select(attrs={'class': 'feedback-input'}), required=True)
    # Primer grupo de opciones
    opciones1 = [('tiktok', 'TikTok'), ('twitter', 'Twitter')]
    redes_sociales1 = forms.MultipleChoiceField(label="", choices=opciones1, widget=forms.CheckboxSelectMultiple(attrs={'class': 'check-content'}), required=False)
    # Segundo grupo de opciones
    opciones2 = [('facebook', 'Facebook'), ('instagram', 'Instagram')]
    redes_sociales2 = forms.MultipleChoiceField(label="", choices=opciones2, widget=forms.CheckboxSelectMultiple(attrs={'class': 'check-content'}), required=False)
    """
    income = forms.DecimalField(
        label="",
        max_digits=10,
        decimal_places=2,
        widget=forms.TextInput(
            attrs={
                'class': 'feedback-input',
                'placeholder': '¿Cuánto ganaste el último mes?',
            }
        )
    )
    """
    income = forms.CharField(label="¿Cuánto ganaste el último mes?", max_length=255, widget=forms.TextInput(attrs={'class': 'feedback-input', 'placeholder': '¿Cuánto ganaste el último mes?'}))
    address = forms.CharField(label="Ingresa tu dirección", max_length=255, widget=forms.TextInput(attrs={'class': 'feedback-input', 'placeholder': 'Ingresa tu dirección'}))
    needs = forms.CharField(label="Ingresa tus necesidades", widget=forms.Textarea(attrs={'class': 'feedback-input', 'placeholder': 'Ingresa tus necesidades'}))
    businessType = forms.CharField(label="Tipo de negocio", max_length=255, widget=forms.TextInput(attrs={'class': 'feedback-input', 'placeholder': 'Tipo de negocio'}))
    niche = forms.CharField(label="Ingresa tu nicho de mercado", max_length=255, widget=forms.TextInput(attrs={'class': 'feedback-input', 'placeholder': 'Ingresa tu nicho de mercado'}))
    businessSize = forms.ChoiceField(label="Tamaño de la empresa", choices=[
        ('', 'Tamaño de la empresa'),
        ('Pequeño', 'Pequeño'),
        ('Mediano', 'Mediano'),
        ('Grande', 'Grande')
    ], widget=forms.Select(attrs={'class': 'feedback-input'}), required=True)
    goals = forms.CharField(label="Ingresa tus objetivos", widget=forms.Textarea(attrs={'class': 'feedback-input', 'placeholder': 'Ingresa tus objetivos'}))
    areaOfInterest = forms.CharField(label="Ingresa tu area de interes", widget=forms.Textarea(attrs={'class': 'feedback-input', 'placeholder': 'En donde te encuentras'}))
    budget = forms.CharField(label="Ingresa tu presupuesto", max_length=255, widget=forms.TextInput(attrs={'class': 'feedback-input', 'placeholder': 'Ingresa tu presupuesto'}))
    time = forms.CharField(label="¿Que edad tiene tu negocio?", max_length=255, widget=forms.TextInput(attrs={'class': 'feedback-input', 'placeholder': '¿Que edad tiene tu negocio?'}))

    """
    def clean_ingresos(self):
        income = self.cleaned_data['income']
        try:
            income = float(income)
        except (TypeError, ValueError):
            raise forms.ValidationError('Ingrese un número válido.')
        if income <= 0:
            raise forms.ValidationError('El número debe ser mayor a cero.')
        return income
    """
