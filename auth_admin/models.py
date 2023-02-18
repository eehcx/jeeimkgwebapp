from django.db import models
from firebase_admin import firestore
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password
from google.cloud import firestore
from django.contrib.auth.models import Group, Permission

class User(models.Model):
    email = models.EmailField(_('email address'), unique=True)
    password = models.CharField(_('password'), max_length=128)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

"""
class FirestoreUser:
    def __init__(self, email, password, timestamp, updated):
        self.email = email
        self.password = password
        self.timestamp = timestamp
        self.updated = updated

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.save_to_firestore()

    def save_to_firestore(self):
        db = firestore.client()
        signup_ref = db.collection(u'users').document(self.email)
        signup_ref.set({
            u'email': self.email,
            u'password': self.password,
            u'timestamp': self.timestamp,
            u'updated': self.updated
        })
"""

