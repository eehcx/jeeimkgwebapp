from django import forms
#from .models import FirestoreUser


"""
class firestoreUserForm(forms.ModelForm):    
    class Meta:
        model = FirestoreUser
        fields = ['email', 'password']

    def save(self, commit=True):
        instance = super(firestoreUserForm, self).save(commit=False)
        instance.save()
        instance.save_to_firestore()
        return instance
"""
