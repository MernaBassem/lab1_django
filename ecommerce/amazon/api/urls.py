from django.urls import path
from .views import *

urlpatterns = [
     path('Hello/',Hello,name='hello') ,
     path('AcceptData/',AcceptData,name='AcceptData'), 
     path('all/',all,name='all') ,
     path('getProduct/<int:id>/',getProduct,name='getProduct') ,
]
