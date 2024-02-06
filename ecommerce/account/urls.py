from django.urls import path, include
from . import views


urlpatterns = [
    path('', include('django.contrib.auth.urls')),  
    path('login/', views.MyLogin, name='myLogin'),
    path('profile/', views.MyProfile, name='profile'),
    path('logout/', views.myLogOut, name='myLogOut'),


]
