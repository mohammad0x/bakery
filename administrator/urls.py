from django.urls import path
from .views import *

app_name = 'administrator'

urlpatterns = [

    path('', landing, name="landing"),

]
