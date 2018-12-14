from __future__ import unicode_literals
from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 1:
            errors['first_name'] = "Field is empty!"
        if len(postData['last_name']) < 1:
            errors['last_name'] = "Field is empty!"
        if len(postData['email']) < 1:
            errors['email'] = "Field is empty!"
        existing_name = User.objects.filter(first_name=postData['first_name'])
        if len(existing_name) > 0:
            errors["first_name"] = "Choose name that does not already exist"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
