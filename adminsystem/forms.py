from django import forms

class EditCustomerForm(forms.Form):
    name = forms.CharField(label='Nombre')
    phoneNumber = forms.CharField(label='Teléfono')
    service = forms.CharField(label='Servicio')
    businessSize = forms.CharField(label='Tamaño de la empresa')
    niche = forms.CharField(label='Nicho')
    businessType = forms.CharField(label='Tipo de empresa')
    email = forms.EmailField(label='Correo electrónico')

    def __init__(self, customer_data, *args, **kwargs):
        super(EditCustomerForm, self).__init__(*args, **kwargs)
        self.fields['name'].initial = customer_data['name']
        self.fields['phoneNumber'].initial = customer_data['phoneNumber']
        self.fields['service'].initial = customer_data['service']
        self.fields['businessSize'].initial = customer_data['businessSize']
        self.fields['niche'].initial = customer_data['niche']
        self.fields['businessType'].initial = customer_data['businessType']
        self.fields['email'].initial = customer_data['email']