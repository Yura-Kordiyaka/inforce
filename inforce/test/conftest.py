import pytest
from employees.models import *


@pytest.fixture
def employee():
    employee = {
        "username": 'yura',
        "email": 'yura@gmail.com',
        "password": 'password',
        "first_name": 'John',
        "last_name": 'Doe',
        "address": '123 Main St',
        "phone_number": '555-1234'
    }
    return employee


@pytest.fixture
def restaurant():
    restaurant = {
        "name": "Lviv",
        "address": "vul. Valova 4, Lviv 79008 Ukraine"
    }
    return restaurant


