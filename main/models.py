from django.db import models

class Product(models.Model):
    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    owner = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    description = models.TextField()