from django.urls import path, include
from dj_rest_auth.views import *

urlpatterns = [
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('login/', LoginView.as_view(), name='rest_login'),
    path('logout/', LogoutView.as_view(), name='rest_logout'),
    path('', UserDetailsView.as_view(), name='rest_user_details'),
]