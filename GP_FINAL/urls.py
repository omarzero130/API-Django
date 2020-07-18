from . import settings
from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('rest_auth.urls')),
    path('user/', include('user.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('products/', include('products.urls')),
    path('orders/',include('order.urls')),
    path('admindashboard/',include('admindashboard.urls')),
]
urlpatterns +=  staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
