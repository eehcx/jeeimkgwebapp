from django.db import models
from firebase_admin import firestore
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.save_to_firestore()

    def save_to_firestore(self):
        db = firestore.Client()
        clients_ref = db.collection('users').document()
        clients_ref.set({
            'email': self.email,
            'password': self.password,
            'timestamp': self.timestamp,
            'updated': self.updated
        })
