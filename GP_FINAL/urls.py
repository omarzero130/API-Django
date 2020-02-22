from . import settings
from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('products/', include('products.urls')),
    path('orders/',include('order.urls')),
    path('user/',include('user.urls')),
    path('admindashboard/',include('admindashboard.urls')),
    path('paypal/',include('paypal.standard.ipn.urls')),
    path('checkout/',include('checkout.urls'))
]

urlpatterns += static('/media/pics/', document_root=settings.MEDIA_ROOT)
