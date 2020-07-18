from django.contrib import admin
from .models import products,category,branch,features,productfeatures,brand_name
# Register your models here.

class productfeaturesAdmin(admin.ModelAdmin):
    list_display=[
        'feat',
        'values'
    ]
    list_filter=[
        'feat','feat__product'
    ]
    search_fields=[
        'value'
    ]

class productfeaturesinlineadmin(admin.TabularInline):
    model=productfeatures
    extra=1

class variationAdmin(admin.ModelAdmin):
    list_display=[
        'product',
        'featurename'   
    ]
    list_filter=[
        'product'
    ]
    search_fields=[
        'name'
    ]
    inlines=[productfeaturesinlineadmin]






admin.site.register(productfeatures,productfeaturesAdmin)
admin.site.register(features,variationAdmin)
admin.site.register(products)
admin.site.register(category)
admin.site.register(branch)
admin.site.register(brand_name)