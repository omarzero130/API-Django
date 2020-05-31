from rest_framework import serializers
from .models import User
from rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from products.serializers import branchserializer
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','id','gender','birthdate','address','avatar','is_superuser','is_staff']

class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','id','gender','birthdate','address','is_staff','avatar']

class UserRegisterationSerializer(RegisterSerializer):
    username=serializers.CharField()
    gender=serializers.CharField()
    birthdate=serializers.DateField()
    address=serializers.CharField()
    class Meta:
        model=User
        fields=['username','email','password','gender','birthdate','address']



    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'gender': self.validated_data.get('gender', ''),
            'birthdate': self.validated_data.get('birthdate', ''),
            'address': self.validated_data.get('address', ''),
            'avatar': self.validate_data.get('avatar','')

        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.username=self.cleaned_data.get('username')
        user.address=self.cleaned_data.get('address')
        user.birthdate=self.cleaned_data.get('birthdate')
        user.gender=self.cleaned_data.get('gender')
        user.avatar=self.cleaned_data.get('avatar')
        user.save()
        adapter.save_user(request, user, self)

        return user

class TokenSerializer(serializers.ModelSerializer):
    user_type=serializers.SerializerMethodField()
    username=serializers.SerializerMethodField()
    avatar=serializers.SerializerMethodField()
    class Meta:
        model=Token
        fields=('key','user','user_type','username','avatar')
    def get_username(self,obj):
        serializer_data=UserSerializer(obj.user).data
        username=serializer_data.get('username')
        return username
    def get_avatar(self,obj):
        serializer_data=UserSerializer(obj.user).data
        ava=serializer_data.get('avatar')
        avatar=f'http://127.0.0.1:8000{ava}'
        return avatar
        
            
    def get_user_type(self,obj):
        serializer_data=UserSerializer(
            obj.user
        ).data
        is_superuser = serializer_data.get('is_superuser')
        is_staff=serializer_data.get('is_staff')
        return{
            'is_superuser':is_superuser,
            'is_staff':is_staff
        }