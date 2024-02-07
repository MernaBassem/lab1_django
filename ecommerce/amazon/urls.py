from django.urls import path,include
from .views import *


urlpatterns = [
    path('',product, name='product'),
    path('add/',add, name='add'),
    path('addForm/',addForm, name='addForm'),
    path('delete_product/<int:product_id>/',delete_product, name='delete_product'),
    path('productUpdateView/<pk>',productUpdateView.as_view(), name='productUpdateView'),
    path('<pk>', ProductDetailView.as_view(), name='productDetail'),
    path('about/',about, name='about'),
    path('category/', category, name='category'),
    path('API/', include('amazon.api.urls')),
    


]



