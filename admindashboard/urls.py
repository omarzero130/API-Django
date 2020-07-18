from django.urls import include, path
from . views import (UsersViewSet,Productstats,productsdelete,Orderstats,productsupdate,
                    Userstats,categoriesViewSet,orderedList,activeList,activeEdit,productscreate,productslist,
                    singleproduct,activeorders,topproducts,topusers,UserUpdate,branchViewSet,singleorder,GetUserOrders,
                    productfeatureslist,addfeatures,singlefeature,deletefeaturesvalues,deletefeatures
                    ,productfeaturesUpdate,featurevaluesUpdate,offers_create,BrandsViewSet)
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'branches', branchViewSet, basename='branches')
router.register(r'users', UsersViewSet, basename='Users')
router.register(r'categories', categoriesViewSet, basename='Categories')
router.register(r'brands', BrandsViewSet, basename='Brands')

urlpatterns = router.urls


urlpatterns = [
    path('',include(router.urls)),
    path('products-list/',productslist.as_view()),
    path('products-delete/<pk>/',productsdelete.as_view()),
    path('products-create/',productscreate.as_view()),
    path('products-update/<pk>/',productsupdate.as_view()),
    path('single-product/<pk>/',singleproduct.as_view()),
    path('activeorders/',activeorders.as_view()),
    path('topproducts/',topproducts.as_view()),
    path('topusers/',topusers.as_view()),
    path('userupdate/',UserUpdate.as_view()),
    path('userscount/',Userstats.as_view()),
    path('orderscount/',Orderstats.as_view()),
    path('Productstats/',Productstats.as_view()),
    path('ordered/',orderedList.as_view()),
    path('active-list/',activeList.as_view()),
    path('active-edit/',activeEdit.as_view()),
    path('single-order/<pk>',singleorder.as_view()),
    path('userorders/',GetUserOrders.as_view()),
    path('features/',productfeatureslist.as_view()),
    path('addfeature/',addfeatures.as_view()),
    path('single-feature/<pk>',singlefeature.as_view()),
    path('feature-update/<pk>',productfeaturesUpdate.as_view()),
    path('featurevalues-update/<pk>',featurevaluesUpdate.as_view()),
    path('feature-delete/<pk>',deletefeatures.as_view()),
    path('featurevalues-delete/<pk>',deletefeaturesvalues.as_view()),
    path('offers-create/',offers_create.as_view())
]