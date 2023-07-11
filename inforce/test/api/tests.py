import pytest
from django.db.models import Count
from rest_framework.test import APIClient
from employees.models import *
from django.urls import reverse
from datetime import datetime
from restaurants.models import *

client = APIClient()


@pytest.mark.django_db
def test_create_employee(employee):
    employee_url = reverse('employee-list')
    response = client.post(employee_url, employee)
    data = response.data
    assert response.status_code == 201
    assert data['username'] == employee['username']


@pytest.mark.django_db
def test_create_menu(restaurant):
    restaurant_url = "http://127.0.0.1:8000/app/v1/restaurant/"
    response_restaurant = client.post(restaurant_url, restaurant)
    assert response_restaurant.status_code == 201
    menu = {
        "dish": "sdfsdfsadfsdafsadf",
        "date": "2023-04-07",
        "restaurant": 1
    }
    menu_url = reverse('menu-list')
    response = client.post(menu_url, menu)
    assert response.status_code == 201
    assert response.data['dish'] == menu['dish']


@pytest.mark.django_db
def test_current_day_menu(restaurant):
    restaurant_url = "http://127.0.0.1:8000/app/v1/restaurant/"
    response_restaurant = client.post(restaurant_url, restaurant)
    assert response_restaurant.status_code == 201
    menu = {
        "dish": "sdfsdfsadfsdafsadf",
        "date": "2023-07-10",
        "restaurant": 2
    }
    menu_url = reverse('menu-list')
    response = client.post(menu_url, menu)
    assert response.status_code == 201
    date = datetime.today().date()
    menu_with_date = Menu.objects.filter(date=date).all()
    assert menu_with_date.count() == 1


@pytest.mark.django_db
def test_the_most_popular_menu(employee, restaurant):
    employee_url = reverse('employee-list')
    client.post(employee_url, employee)
    restaurant_url = "http://127.0.0.1:8000/app/v1/restaurant/"
    response_restaurant = client.post(restaurant_url, restaurant)
    assert response_restaurant.status_code == 201
    menu = {
        "dish": "sdfsdfsadfsdafsadf",
        "date": "2023-07-10",
        "restaurant": 3
    }
    menu_url = "http://127.0.0.1:8000/app/v1/menu/"
    response_menu = client.post(menu_url, menu)
    assert response_menu.status_code == 201
    vote = {
        "employee": 2,
        "menu": 3
    }
    vote_url = reverse('vote-list')
    client.post(vote_url, vote)
    response_vote = client.post(vote_url, vote)
    assert response_vote.status_code == 201
    vote_item = Vote.objects.all()
    assert vote_item.count() == 2
    date = datetime.today().date()
    menu_with_date = Menu.objects.filter(date=date).all()
    votes = Vote.objects.values('menu').annotate(vote_count=Count('employee'))
    results = []
    for menu in menu_with_date:
        vote_count = 0
        for result in votes:
            if result['menu'] == menu.id:
                vote_count = result['vote_count']
                break
        result = {
            'menu': {
                'id': menu.id,
                'restaurant': menu.restaurant.name,
                'dish': menu.dish,
                'date': menu.date.strftime('%Y-%m-%d')
            },
            'vote_count': vote_count
        }
        results.append(result)
    results = sorted(results, key=lambda x: x['vote_count'], reverse=True)
    assert results[0]['vote_count'] == 2
    assert results[0]['menu']['id'] == 3


@pytest.mark.django_db
def test_token_creation():
    employee = Employee.objects.create_user(username='yura', email='yura@gmail.com', password='1234',
                                            address='asdfsdfa', phone_number='02134234234', first_name='asdf',
                                            last_name='asdf')
    response = client.post(reverse('token_obtain_pair'), data={'username': 'yura', 'password': '1234'},
                           format='json')
    assert response.status_code == 200

    token = response.data['access']
    # print('sadfsadfasdfasdf')
    assert token is not None


@pytest.mark.django_db
def test_do_vote(restaurant):
    employee = Employee.objects.create_user(username='ivan', email='yura@gmail.com', password='1234',
                                            address='asdfsdfa', phone_number='02134234234', first_name='asdf',
                                            last_name='asdf')

    response = client.post(reverse('token_obtain_pair'), data={'username': 'ivan', 'password': '1234'}, format='json')
    assert response.status_code == 200

    token = response.data['access']
    print(token)
    assert token is not None
    headers = {'Authorization': f'Bearer {str(token)}'}
    restaurant_url = "http://127.0.0.1:8000/app/v1/restaurant/"
    response_restaurant = client.post(restaurant_url, restaurant)
    menu = {
        "dish": "sdfsdfsadfsdafsadf",
        "date": "2023-07-10",
        "restaurant": 4
    }
    menu_url = reverse('menu-list')
    response_menu = client.post(menu_url, menu)
    vote = {
        "employee": 4,
        "menu": 4
    }
    assert response_menu.data['id'] == 4
    assert employee.id == 4
    do_vote_url = 'http://127.0.0.1:8000/app/v1/employee/do_vote/'
    client.post(do_vote_url, vote, headers=headers)
    vote = Vote.objects.all()
    assert vote.count() == 1
