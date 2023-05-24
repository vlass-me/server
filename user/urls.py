from django.urls import path, include
from dj_rest_auth.views import *
from dj_rest_auth.registration.views import *
from rest_framework.routers import DefaultRouter
from .views import SessionViewSet

router = DefaultRouter()

router.register('session', SessionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('registration/', RegisterView.as_view(), name='rest_register'),
    path('login/', LoginView.as_view(), name='rest_login'),
    path('logout/', LogoutView.as_view(), name='rest_logout'),
    path('info/', UserDetailsView.as_view(), name='rest_user_details'),
]
