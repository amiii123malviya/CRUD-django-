from django.urls import path
from .views import *

urlpatterns=[

    path('home/',home,name='home'),
    path('insert/',insert,name='insert'),
    path('showdata/',showdata,name='showdata'),
]