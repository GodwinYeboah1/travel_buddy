from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.contrib import messages
from django.utils import timezone
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
        
        if len(userData["name"]) < 3: 
            response["errors"].append('user name must be 3 charater and greater')
            response['valid'] = False

        if len(userData["password"]) < 8: 
            response["errors"].append('password name must be 8 charater and greater')
            response['valid'] = False

        if len(userData["password"] != userData["confirm_password"]):
            response['errors'].append('Your password does not match')
            response['valid'] = False
        else:
            if response['valid']:
                userData.save(
                    name=userData['name'], 
                    username=userData['username'], 
                    password=userData['password']
                )


class TripManger(models.Manager):
    
    def trip_validation(self, tripData):
        
        response = {
            'errors' : [],
            'trip': None,
            'valid': True
        }

        if len(tripData['destination']) < 0:
            response['errors'].append("You must add a destination")
            response['valid'] = False   
        if len(tripData['description']) < 0:
            response['errors'].append("You must add a description")
            response['valid'] = False 
        else:
            if response['valid']:
                tripData.save(
                    user = tripData['user'], 
                    destination= tripData['destination'], 
                    description= tripData['description'], 
                    travel_date_from = tripData['travel_date_from'], 
                    travel_date_to = tripData['travel_date_to'], 
                )
                


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    object  = UserManger()

class Trip(models.Model):
    user = models.ForeignKey(User)
    destination = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    travel_date_from = models.DateField()
    travel_date_to = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    object  = TripManger()

