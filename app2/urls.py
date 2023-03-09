from app2.views import *
from django.urls import path
app_name='mi'
urlpatterns=[
    path('rohit/',rohit,name='rohit'),
    path('surya/',surya,name='surya'),
]