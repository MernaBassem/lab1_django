from django.urls import path
from . import views


urlpatterns = [
    path('', views.categoryList, name='categoryList'),
    path('addCategory/', views.addCategory, name='addCategory'),
    path('delete_category/<int:category_id>/', views.delete_category, name='delete_category'),

]
