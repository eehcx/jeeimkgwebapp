from django.db import models
from firebase_admin import firestore

class Contact(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.save_to_firestore()
    
    def save_to_firestore(self):
        db = firestore.client()
        contact_ref = db.collection('contacts').document()
        contact_ref.set({
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'message': self.message,
            'created_at': self.created_at,
        })
