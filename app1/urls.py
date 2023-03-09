from app1.views import *
from django.urls import path
app_name='rcb'
urlpatterns=[
    path('virat/',virat,name='virat'),
    path('abd/',abd,name='abd'),
]