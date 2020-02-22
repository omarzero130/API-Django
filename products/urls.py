from django.urls import include, path

from .views import (productslist,productscreate,
                    categoryviewset,productsdelete,productfilter)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
#router.register('branch', branchviewset, basename='branch')
router.register('category', categoryviewset, basename='category')


urlpatterns = [
    path('',include(router.urls)),
    path('products-list/',productslist.as_view()),
    path('products-list/<pk>',productsdelete.as_view()),
    path('create/',productscreate.as_view()),
    path('productfilter/',productfilter.as_view())
]