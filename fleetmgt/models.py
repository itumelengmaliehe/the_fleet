from django.db import models

# Create your models here.
class fleetVehicle(models.Model):
    plate_no = models.CharField (max_length=30)
    registration_no = models.CharField (max_length=30)
    eng_no = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    colour = models.CharField(max_length=30)
    year = models.CharField(max_length=30)

