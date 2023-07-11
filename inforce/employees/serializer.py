from rest_framework import serializers
from .models import *


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','username', 'email', 'first_name', 'last_name', 'address', 'phone_number','password']
