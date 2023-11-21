from django.urls import path
from menu.core import views as v


app_name = 'menu.core'


urlpatterns = [
    path('api/users/', v.api_users, name='users'),
]