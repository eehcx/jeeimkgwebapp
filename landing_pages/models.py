from django.db import models
from firebase_admin import firestore


# class Client(models.Model):
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    business_type = models.CharField(max_length=100)
    service = models.CharField(max_length=100)
    social_media = models.CharField(max_length=100)
    monthly_revenue = models.PositiveIntegerField()
    address = models.CharField(max_length=100)
    needs = models.TextField()
    final_price = models.DecimalField(max_digits=10, decimal_places=2)

    def save_to_firestore(self):
        db = firestore.Client()
        clients_ref = db.collection('clients')
        new_client_ref = clients_ref.document()

        new_client_ref.set({
            'name': self.name,
            'email': self.email,
            'phone_number': self.phone_number,
            'business_type': self.business_type,
            'service': self.service,
            'social_media': self.social_media,
            'monthly_revenue': self.monthly_revenue,
            'address': self.address,
            'needs': self.needs,
            'final_price': self.final_price,
        })