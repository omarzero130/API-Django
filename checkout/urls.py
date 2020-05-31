from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static
from .views import checkout,payment_canceled,payment_done

app_name='payment'
urlpatterns = [
    path('', checkout),
    path('done/',payment_done,name='done'),
    path('canceled',payment_canceled,name='canceled')
  
]
