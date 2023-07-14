from django.db import models
from django.contrib.auth.models import AbstractUser
from restaurants.models import Menu



class Employee(AbstractUser):
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)


class Vote(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    vote_datetime = models.DateTimeField(auto_now_add=True)
