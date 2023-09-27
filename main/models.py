from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    amount = models.IntegerField(validators=[MinValueValidator(0)])
    date_added = models.DateField(auto_now_add=True)
    description = models.TextField()