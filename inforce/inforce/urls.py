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
    path('admin/', admin.site.urls),
    path('app/v1/', include(router.urls)),
    # path('app/v2/', include("inforce.urlsv2")),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
