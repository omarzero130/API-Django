from rest_framework import serializers
from .models import products,branch_products,category,branch

class string(serializers.StringRelatedField):
    def to_internal_value(self, data):
        return data

class categoryserializer(serializers.ModelSerializer):
    class Meta:
        model=category
        fields=['name','id']


class branchserializer(serializers.ModelSerializer):


    class Meta:
        model=branch
        fields=['name','QR_code','id']


class productsserializer(serializers.ModelSerializer):
    category=serializers.SerializerMethodField()
    branch=serializers.SerializerMethodField()
    class Meta:
        model=products
        fields=['name','Barcode','price','description','image','id','category','branch']
    def get_category(self,obj):
        return categoryserializer(obj.category).data
    def get_branch(self,obj):
        return branchserializer(obj.branch).data
class productscreateserializer(serializers.ModelSerializer):
    class Meta:
        model=products
        fields=['name','Barcode','price','description','image','category']

