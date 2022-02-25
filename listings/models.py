from django.db import models
from django.contrib.auth.models import (AbstractUser, PermissionsMixin)
from django.conf import settings
from .managers import UserManager

class User(AbstractUser):
    
    username = models.CharField(max_length=128,unique=True)
    team = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username


class Client(models.Model):

    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=254, unique=True)
    mobile = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    company_name = models.CharField(max_length=128)
    sales_contact = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='main_assignee')

    def __str__(self):
        return self.last_name


class Contract(models.Model):
    
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE, related_name='contract_client')
    amount = models.CharField(max_length=128)
    sales_contact = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='sales_assignee')
    status = models.CharField(max_length=128)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.id


class Event(models.Model):

    name = models.CharField(max_length=128)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE, related_name='event_client')
    support_contact = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='support_assignee')
    contract = models.ForeignKey(to=Contract, on_delete=models.CASCADE, related_name='contract')
    status = models.CharField(max_length=128)
    attendees = models.CharField(max_length=128)
    date_event = models.DateTimeField()
    notes = models.CharField(max_length=128)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name