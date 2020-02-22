from django.urls import include, path
from .views import CurrentUserView

urlpatterns = [

    #path('rest-auth/google/', GoogleLogin.as_view(), name='fb_login'),
    path('current/',CurrentUserView.as_view())

]