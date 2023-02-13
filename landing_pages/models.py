from django.db import models
from firebase_admin import firestore


# clase en proceso, no terminada
class clients(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=120, blank=True, null=True)
    phone_number = models.CharField(max_length=120, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def save_to_firestore(self):
        db = firestore.client()
        signup_ref = db.collection(u'clients').document()
        signup_ref.set({
            u'email': self.email,
            u'full_name': self.full_name,
            u'timestamp': self.timestamp,
            u'updated': self.updated
        })
