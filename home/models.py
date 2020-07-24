from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def basic_validator(self, formData):
        errors = {}
        if len(formData['fname']) < 2:
            errors["fname"] = "First Name should be at least 3 characters"
        if len(formData['lname']) < 2:
            errors["lname"] = "Last Name should be at least 3 characters"
        if not EMAIL_REGEX.match(formData['email']):
            errors['email'] = 'Invalid Email Address'
        email_check = self.filter(email=formData['email'])
        if email_check:
            errors['email'] = "Email already in use"
        if len(formData['pwrd']) < 5:
            errors["pwrd"] = "Password should be at least 8 characters"
        if len(formData['pwrd']) < 8:
            errors['pwrd'] = 'Password must be at least 8 characters'     
        if formData['pwrd'] != formData['conpwrd']:
            errors['pwrd'] = 'Passwords do not match'
        return errors

    def register(self, formData):
        pw_hash = bcrypt.hashpw(formData['pwrd'].encode(), bcrypt.gensalt()).decode()
        return self.create(
            first_name = formData['fname'],
            last_name = formData['lname'],
            email = formData['email'],
            password = pw_hash
            )   
            
    def authenticate(self, email, password):
        users = self.filter(email=email)
        if not users:
            return False

        user = users[0]
        return bcrypt.checkpw(password.encode(), user.password.encode())

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

