from django.urls import path
from .views import *


urlpatterns = [
    path('',product, name='product'),
    path('add/',add, name='add'),
    path('addForm/',addForm, name='addForm'),
    path('delete_product/<int:product_id>/',delete_product, name='delete_product'),
    path('productUpdateView/<pk>',productUpdateView.as_view(), name='productUpdateView'),

    # path('<pk>', productDetail.as_view(), name='productDetail'),
    path('<pk>', ProductDetailView.as_view(), name='productDetail'),
    # path('productDetail/<int:productID>/', productDetail, name='productDetail'),
    # path('UpdateForm/<int:productID>/',UpdateForm, name='ProductUpdateView'),
    path('about/',about, name='about'),
    path('category/', category, name='category'),


]

   # path('update/<int:productID>/', views.update, name='update'),
    # path('UpdateForm/<int:productID>/', views.UpdateForm, name='UpdateForm'),


