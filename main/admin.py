from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Address)
admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Category)