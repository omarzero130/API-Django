from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from rest_framework.views import APIView

from rest_framework.generics import RetrieveAPIView 
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from user.models import User
from rest_framework.authtoken.models import Token

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    callback_url = 'http://localhost:8000/accounts/google/login/callback/'


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
  

class CurrentUserView(RetrieveAPIView):
    serializer_class=UserSerializer
    def get_object(self):
        print(self.request.META.get('HTTP_AUTHORIZATION'))
        token=self.request.META.get('HTTP_AUTHORIZATION')
        use=Token.objects.get(key=token).user
        user=User.objects.get(username=use)
        return user

