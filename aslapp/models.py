from django.db import models

class Sign(models.Model):
    image = models.CharField(max_length=800)
    name = models.CharField(max_length=100)
    notes = models.CharField(max_length=2000)
    date = models.DateField(auto_now_add=True)

