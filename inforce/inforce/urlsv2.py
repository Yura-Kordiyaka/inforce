from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework.routers import DefaultRouter
from employees.views import *
from restaurants.views import *


router = DefaultRouter()

router.register(r'employee', EmployeeViewSet, basename='employee')
router.register(r'restaurant', RestaurantViewSet, basename='restaurant')
router.register(r'menu', MenuViewSet, basename='menu')
router.register(r'vote', VoteViewSet, basename='vote')

urlpatterns = [
    path('', include(router.urls)),
]
