from rest_framework import  serializers
from.models import orders,order_details,wishlist,wishlistdetails,review
from products.serializers import productsserializer

class string(serializers.StringRelatedField):
    def to_internal_value(self, data):
        return data


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


class orderListSerializer(serializers.ModelSerializer):
    user=string()
    total_price=serializers.SerializerMethodField()
    items=serializers.SerializerMethodField()
    class Meta:
        model=orders
        fields=['user','ordered','total_price','id','items']
    def get_total_price(self,obj):
        return obj.total()
    def get_items(self,obj):
        return orderdetails(obj.items.all(),many=True).data

class chartserializer(serializers.ModelSerializer):
    class Meta:
        model=order_details
        fields=['product','quantity','id']


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
        return productbranchSerializer(obj.product).data


class reviewserializer(serializers.ModelSerializer):
    user=string()
    class Meta:
        model=review
        fields=['id','body','user']