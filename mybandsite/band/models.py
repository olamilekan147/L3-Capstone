from django.db import models


class Member(models.Model):
    """
    Represent and member object
    
    :param models.models (object): the model parent class.
    """
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField()


class Event(models.Model):
    """
    Represent and event object
    
    :param models.models (object): the model parent class.
    """
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
