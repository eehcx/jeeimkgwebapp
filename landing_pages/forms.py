from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone_number', 'business_type', 'service', 'social_media', 'monthly_revenue', 'address', 'needs', 'final_price']

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'email'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'phone_number'}))
    # business_type = forms.ChoiceField(choices=BUSINESS_TYPE_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'id': 'business_type'}))
    service = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'service'}))
    social_media = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'social_media'}))
    monthly_revenue = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'monthly_revenue'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'address'}))
    needs = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'needs'}))
    final_price = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'final_price'}))

    def save(self, commit=True):
        instance = super(ClientForm, self).save(commit=False)
        if commit:
            instance.save()
            instance.save_to_firestore()
        return instance
