from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=250, default="Cardiothoracic Surgeon")
    fees = models.DecimalField(max_digits=10, decimal_places=2, default=300)
    contact_info = models.CharField(max_length=20)
    address = models.CharField(max_length=250)
    recommendation = models.PositiveIntegerField(default=6)
    gender = models.CharField(max_length=200, default="Female")
    hospital = models.CharField(max_length=200, default="CMC")
    email = models.CharField(max_length=254, blank=True, null=True)
    experience = models.PositiveIntegerField(default=5)

    def __str__(self):
        return self.name
