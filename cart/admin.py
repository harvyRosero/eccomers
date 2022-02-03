from django.contrib import admin
from .models import (
    Product, 
    Order, 
    OrderItem ,
    ColourVariation,
    SizeVariation,
    Address,
    Payment
    )

class AdressAdmin(admin.ModelAdmin):
    list_display = [
        'adress_line_1',
        'adress_line_2',
        'zip_code',
        'city',
        'adress_type',
    ] 

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ColourVariation)
admin.site.register(SizeVariation)
admin.site.register(Address, AdressAdmin)
admin.site.register(Payment)
