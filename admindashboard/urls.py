from django.urls import include, path
from . views import UsersViewSet,categoriesViewSet,ordersViewSet,productscreate,productslist,singleproduct,activeorders,topproducts,topusers
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'orders', ordersViewSet, basename='orders')
router.register(r'users', UsersViewSet, basename='Users')
router.register(r'categories', categoriesViewSet, basename='Categories')
urlpatterns = router.urls


urlpatterns = [
    path('',include(router.urls)),
    path('products-list/',productslist.as_view()),
    path('products-create/',productscreate.as_view()),
    path('single-product/<pk>/',singleproduct.as_view()),
    path('activeorders/',activeorders.as_view()),
    path('topproducts/',topproducts.as_view()),
    path('topusers/',topusers.as_view())



]