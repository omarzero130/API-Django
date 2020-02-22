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
        fields=['QR_code','id']


class productsserializer(serializers.ModelSerializer):
    category=serializers.SerializerMethodField()
    class Meta:
        model=products
        fields=['name','Barcode','price','description','image','id','category']
    def get_category(self,obj):
        return categoryserializer(obj.category).data

class productscreateserializer(serializers.ModelSerializer):
    class Meta:
        model=products
        fields=['name','Barcode','price','description','image','category']


'''
class productbranchSerializer(serializers.ModelSerializer):
    product=serializers.SerializerMethodField()
    branch=serializers.SerializerMethodField()
    class Meta:
        model=branch_products
        fields=['product','branch','price','prev_price','quantity','id']


    def get_product(self,obj):
        return productsserializer(obj.product).data
    def get_branch(self,object):
        return branchserializer(object.branch).data


class productbranchcreateSerializer(serializers.ModelSerializer):

    class Meta:
        model=branch_products
        fields=['product','branch','price','prev_price','quantity','id']

'''