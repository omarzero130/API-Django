from django.urls import include, path
from .views import GoogleLogin,CurrentUserView,FacebookLogin

urlpatterns = [

    path('rest-auth/google/', GoogleLogin.as_view(), name='fb_login'),
    path('rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('current/',CurrentUserView.as_view())
]