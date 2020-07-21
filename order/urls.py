from django.urls import include, path
from . views import (orderslist,submitorder,addtocart,orderdetails,review,deletefromcart,
                    orderdetailsquantity,topuserproducts,Addtowhitelist,whitelistList,deleteFromWhitelist)



urlpatterns = [
    path('',orderslist.as_view()),
    path('addtocart/',addtocart.as_view()),
    path('cart/',orderdetails.as_view()),
    path('addreview/',review.as_view()),
    path('deletefromcart/<pk>/',deletefromcart.as_view()),
    path('orderdetailsquantity/',orderdetailsquantity.as_view()),
    path('checkout/',submitorder.as_view()),
    path('orderslist/',orderslist.as_view()),
    path('topuserproducts/',topuserproducts.as_view()),
    path('whitelistadd/',Addtowhitelist.as_view()),
    path('whitelist/',whitelistList.as_view()),
    path('deletefromwhitelist/<pk>',deleteFromWhitelist.as_view())
    



]