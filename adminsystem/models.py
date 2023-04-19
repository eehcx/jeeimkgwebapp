from django.db import models

class Cliente(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=20)
    income = models.DecimalField(max_digits=10, decimal_places=2)
    sector = models.CharField(max_length=255)
    needs = models.CharField(max_length=255)
    socialMedia = models.CharField(max_length=255)
    service = models.CharField(max_length=255)
    businessType = models.CharField(max_length=255)
    niche = models.CharField(max_length=255)
    businessSize = models.CharField(max_length=255)
    goals = models.CharField(max_length=255)
    areaOfInterest = models.CharField(max_length=255)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.CharField(max_length=255)
    creationDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
