from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        # check first_name
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name field is empty!"
        # check last_name
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name field is empty!"
        # # check email
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid Email Address!"
        # # check password
        if len(postData['password']) < 8:
            errors["password"] = "Password must be at least 8 characters"
        elif postData['password'] != postData['confirm_password']:
            errors['password'] = "Password must match!"

        return errors

    def login_validator(self, postData):
        errors={}
        # check Email
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid Email Address!"
        # elif postData['email'] != User.objects.filter(email=postData['email'])
        # # check password
        if len(postData['password']) < 8:
            errors["password"] = "Password must be at least 8 characters"

        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
