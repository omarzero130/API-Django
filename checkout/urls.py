from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static
from .views import payment_canceled,payment_done,Checkout2

app_name='payment'
urlpatterns = [
    path('',Checkout2.as_view()),
    path('done/',payment_done,name='done'),
    path('canceled',payment_canceled,name='canceled')
  
]
