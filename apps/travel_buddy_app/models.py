from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.contrib import messages
import bcrypt

class UserManger(models.Manager):
    pass
    def register_validation(self, userData):
        # catch error system 
        response = {
            'errors': [],
            'user': None,
            'valid': True
        }
        # need to greater then 3 
        if len(userData["name"]) < 3: 
            response["errors"].append('user name must be 3 charater and greater');
            response['valid'] = False;

        if len(userData["password"]) < 8: 
            response["errors"].append('password name must be 8 charater and greater');
            response['valid'] = False;

        if len(userData["password"] != userData["confirm_password"]):
            response['errors'].append('Your password does not match');
            response['valid'] = False;

        else:
            pass
          

    



# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Trip(models.Model):
    trip_by = models.ForeignKey(User, related_name="trip_by_user")
    destination = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    travel_date_from = models.DateField()
    travel_date_to = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

