from django.db import models
from django.urls import reverse
from datetime import datetime

# Create your models here.
class charitydata(models.Model):
    domains= (
        ('N', 'Natural calamities'),
        ('T', 'TerrorAttack'),
        ('C','Climaticproblems'),
        ('F','Farmerproblems'),
    )
    year_in_school = models.CharField(max_length=2,choices=domains,)

   
    Charity_domain=models.CharField(max_length=100,choices=domains)
    Donor_name = models.CharField(max_length=200)
    Donation_date = models.DateTimeField(default=datetime.now, blank=True)
    Donation_amount=models.FloatField()

    def __str__(self):
        return self.name
