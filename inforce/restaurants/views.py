from datetime import datetime
from django.db.models import Count
from rest_framework import  viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from employees.models import *
from .serializer import *


# Create your views here.
class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    @action(methods=['get'], detail=False)
    def take_menu_by_date(self, request):
        data = request.data
        date = datetime.today().date()
        menu_with_date = Menu.objects.filter(date=date).all()
        if menu_with_date:
            return Response({'menu': MenuSerializer(menu_with_date, many=True).data})
        else:
            return Response({'news': 'is that there is no menu for that date'})

    @action(methods=['get'], detail=False)
    def the_most_popular_menu(self, request):
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
        return Response({'results': results})
