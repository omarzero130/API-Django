from django.contrib import admin
from .models import products,category,branch,branch_products
# Register your models here.

admin.site.register(products)
admin.site.register(category)
admin.site.register(branch_products)
admin.site.register(branch)