from django.urls import path, include
from .views import *


urlpatterns = [
    path('', include('django.contrib.auth.urls')),  
    path('login/', MyLogin, name='myLogin'),
    path('profile/', MyProfile, name='profile'),
    path('logout/', myLogOut, name='myLogOut'),
    path('register/',myRegister.as_view(),name="myRegister"),

]
