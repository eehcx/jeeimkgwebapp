from django.db import models
from firebase_admin import firestore

class Contact(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)