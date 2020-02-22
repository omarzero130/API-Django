from rest_framework import serializers
from .models import User
from rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from products.serializers import branchserializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"

class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password','id','gender','birthdate','address']

class UserRegisterationSerializer(RegisterSerializer):
    username=serializers.CharField()
    gender=serializers.CharField()
    birthdate=serializers.DateField()
    address=serializers.CharField()
    class Meta:
        model=User
        fields=['username','email','password','gender','birthdate','address','is_staff','is_superuser']

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'gender': self.validated_data.get('gender', ''),
            'birthdate': self.validated_data.get('birthdate', ''),
            'address': self.validated_data.get('address', ''),

        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.username=self.cleaned_data.get('username')
        user.address=self.cleaned_data.get('address')
        user.birthdate=self.cleaned_data.get('birthdate')
        user.gender=self.cleaned_data.get('gender')
        user.save()
        adapter.save_user(request, user, self)

        return user