from rest_framework import serializers
from .models import products,category,branch,features,productfeatures,limited_offers

class string(serializers.StringRelatedField):
    def to_internal_value(self, data):
        return data

class FeatureValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model=productfeatures
        fields=['id','values']
   

class ProductFeaturesSerializer(serializers.ModelSerializer):
    values=serializers.SerializerMethodField()
    product=string()
    class Meta:
        model=features
        fields=['id','featurename','values','product']
    def get_values(self,obj):
        return FeatureValuesSerializer(obj.productfeatures_set.all(),many=True).data


class categoryserializer(serializers.ModelSerializer):
    class Meta:
        model=category
        fields=['name','id']


class branchserializer(serializers.ModelSerializer):


    class Meta:
        model=branch
        fields=['name','QR_code','id']


class productsserializer(serializers.ModelSerializer):
    category=string()
    branch=serializers.SerializerMethodField()
    feature=serializers.SerializerMethodField()
    featurecount=serializers.SerializerMethodField()
    class Meta:
        model=products
        fields=['name','Barcode','description','discount_price','image','id','category','price','feature','featurecount','branch']
    def get_feature(self,obj):
        return ProductFeaturesSerializer(obj.features_set.all(),many=True).data
    def get_featurecount(self,obj):
        return obj.features_set.count()
    def get_branch(self,obj):
        return branchserializer(obj.branch).data
class productscreateserializer(serializers.ModelSerializer):
    class Meta:
        model=products
        fields=['name','Barcode','description','image','price','category','branch']


class limitedoffersserializer(serializers.ModelSerializer):
    class Meta:
        model=limited_offers
        fields=['product','new_price','end_date','start_date']