from django.db import models

# Create your models here.

class User(models.Mode):

    id = models.IntegerField(primary_key=True, null=False)
    name = models.TextField(blank=False, null=False)
    age = models.IntegerField(blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    dob = models.DateField(null=False)
    disease = models.TextField(max_length=254, null=True)
    admit_date = models.DateField(null=False)
    discharge_date = models.DateField(null=False)
    location = models.TextField(blank=True)
    contact_no = models.TextField(max_length=10, null=False)
    
