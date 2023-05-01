from django.urls import path
from .views import index, add_book, add_user, update_user, delete_user, product_detail, add_product

urlpatterns = [
    path('', index, name="index"),
    path('<slug:cat_slug>/', index, name="cat_detail"),
    path('add/product/', add_product, name='add_product'),
    path('product/<int:pk>/', product_detail, name="product_detail"),
    path('add/book/', add_book, name="add_book"),
    path('add/user/', add_user, name="add_user"),
    path('update/<int:pk>/', update_user, name="update_user"),
    path('delete/<int:pk>/', delete_user, name="delete_user")
]