from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['email', 'full_name']

    def save(self, commit=True):
        instance = super(SignUpForm, self).save(commit=False)
        instance.save()
        instance.save_to_firestore()
        return instance
