from django.urls import path
from app2.views import *

app_name='RCB'
urlpatterns=[
    path('team2/',team2,name='team2')
]