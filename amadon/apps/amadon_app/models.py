from __future__ import unicode_literals
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    

class Item(models.Model):
    item = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    user = models.ForeignKey(User, related_name="items")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
