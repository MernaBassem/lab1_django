from django.urls import path
from . import views


urlpatterns = [
    path('', views.categoryList, name='categoryList'),
    path('addCategory/', views.addCategory, name='addCategory'),
    path('categoryUpdateView/<pk>', views.categoryUpdateView.as_view(), name='categoryUpdateView'),
    # path('delete_category/<int:category_id>/', views.delete_category, name='delete_category'),
    path('delete_category/<pk>/', views.delete_category.as_view(), name='delete_category'),

]
