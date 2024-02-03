from django.urls import path
from . import views

urlpatterns = [
    path('', views.product, name='product'),
    path('add/', views.add, name='add'),
    path('productDetail/<int:productID>/', views.productDetail, name='productDetail'),
    path('about/', views.about, name='about'),
    path('category/', views.category, name='category'),
]
