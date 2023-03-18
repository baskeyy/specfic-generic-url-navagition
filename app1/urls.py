from django.urls import path
from app1.views import *

app_name='CSK'
urlpatterns=[
    path('team1/',team1,name='team1')
]