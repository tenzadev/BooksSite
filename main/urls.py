from django.urls import path
from .views import main_page, about_page, contact_page, add_order

urlpatterns = [
    path('', main_page),
    path('contact/', contact_page),
    path('about/', about_page),
    path('add/order/', add_order, name="add_order")
]
