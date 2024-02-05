from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('', views.product, name='product'),
    path('add/', views.add, name='add'),
    path('addForm', views.addForm, name='addForm'),
     path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('productDetail/<int:productID>/', views.productDetail, name='productDetail'),
    path('update/<int:productID>/', views.update, name='update'),
    path('about/', views.about, name='about'),
    path('category/', views.category, name='category'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
