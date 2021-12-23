from django.urls import path
from .views import *


urlpatterns = [
    path('', sign_in, name='signin'),
    path('signup/', sign_up, name='signup'),
    path('signout/', sign_out, name='signout'),
]