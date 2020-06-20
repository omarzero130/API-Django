from django.urls import include, path
from . views import orderslist,submitorder,addtocart,orderdetails,review,deletefromcart,orderdetailsquantity



urlpatterns = [
    path('',orderslist.as_view()),
    path('addtocart/',addtocart.as_view()),
    path('cart/',orderdetails.as_view()),
    path('addreview/',review.as_view()),
    path('deletefromcart/<pk>/',deletefromcart.as_view()),
    path('orderdetailsquantity/',orderdetailsquantity.as_view()),
    path('checkout/',submitorder.as_view()),


]