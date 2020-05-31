from rest_framework import  serializers
from.models import orders,order_details,wishlist,wishlistdetails,review
from products.serializers import productsserializer
from products.serializers import ProductFeaturesSerializer



class string(serializers.StringRelatedField):
    def to_internal_value(self, data):
        return data


class orderdetailsserializer(serializers.ModelSerializer):
    product=string()
    product_obj=serializers.SerializerMethodField()
    price=serializers.SerializerMethodField()
    class Meta:
        model=order_details
        fields=['product','quantity','id','product_obj','price']
    def get_product_obj(self,obj):
        return productsserializer(obj.product).data
    def get_price(self,obj):
        return obj.final_price()
   


class orderdetails(serializers.ModelSerializer):
    product=serializers.SerializerMethodField()
    final_price=serializers.SerializerMethodField()
    class Meta:
        model=order_details
        fields=['product','quantity','id','final_price']
    def get_product(self,obj):
        return productsserializer(obj.product).data
    def get_final_price(self,obj):
        return obj.price()
class chartserializer(serializers.ModelSerializer):
    product=serializers.SerializerMethodField()
    
    class Meta:
        model=order_details
        fields=['product','quantity','id']
    def get_product(self,obj):
            return productsserializer(obj.product).data


class orderListSerializer(serializers.ModelSerializer):
    user=string()
    items=serializers.SerializerMethodField()
    total=serializers.SerializerMethodField()
   
    class Meta:
        model=orders
        fields=['user','ordered','id','items','total','created_at']

    def get_items(self,obj):
        return orderdetailsserializer(obj.items.all(),many=True).data
    def get_total(self,obj):
        return obj.total()
   


class wishlistserializer(serializers.ModelSerializer):
    user=string()
    items=serializers.SerializerMethodField()
    class Meta:
        model=wishlist
        fields=['user','id','items']

    def get_items(self,obj):
        return orderdetails(obj.items.all(),many=True).data

class wishlistdetailsserializer(serializers.ModelSerializer):
    product=serializers.SerializerMethodField()

    class Meta:
        model = wishlistdetails
        fields = ['product', 'id']

    def get_product(self, obj):
        return productsserializer(obj.product).data


class reviewserializer(serializers.ModelSerializer):
    user=string()
    class Meta:
        model=review
        fields=['id','body','user']