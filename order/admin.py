from django.contrib import admin
from .models import orders,order_details,wishlist,wishlistdetails
# Register your models here.
admin.site.register(orders)
admin.site.register(order_details)
admin.site.register(wishlist)
admin.site.register(wishlistdetails)
