from django.db import models

'''
This class was written by Travis for our group project.
'''

class Fosters(models.Model):
    fosterID = models.IntegerField(unique=True, primary_key=True)
    fosterName = models.CharField(max_length=50)
    fosterEmail = models.EmailField(max_length=70)
    fosterPhone = models.CharField(max_length=10)
    fosterStreet = models.CharField(max_length=50)
    fosterCity = models.CharField(max_length=50)
    fosterState = models.CharField(max_length=2)
    fotserZip = models.CharField(max_length=5)
