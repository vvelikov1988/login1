from django.db import models
from datetime import datetime


class Manager(models.Manager):
    def basic_validator(self, formData):
        errors = {}
        if len(formData['fname']) < 2:
            errors["fname"] = "First Name should be at least 3 characters"
        if len(formData['lname']) < 2:
            errors["lname"] = "Last Name should be at least 3 characters"
        if len(formData['network']) < 3:
            errors["network"] = "Network should be at least 3 characters"
        if formData['desc'] != '' and len(formData['desc']) < 10:
            errors['desc'] = "Description should be at least 10 characters"
        if datetime.strptime(formData['reldate'], '%Y-%m-%d') > datetime.now():
            errors['reldate'] = "Release Date should be in the past"
        return errors

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.DateField(max_length=255)
    password = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Manager()
