from django.shortcuts import render
from products.models import products,category
from user.models import User
from order.models import orders,order_details,wishlist,wishlistdetails,review
from order.serializers import orderListSerializer
from rest_framework import viewsets
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView
from products.serializers import productsserializer,categoryserializer,productscreateserializer
from order.serializers import chartserializer
from user.serializers import UserSerializer
from rest_framework.response import Response


class productslist(ListAPIView):
    queryset = products.objects.all().order_by('-id')
    serializer_class = productsserializer


class singleproduct(RetrieveAPIView):
    queryset = products.objects.all()
    serializer_class = productsserializer   

class productscreate(CreateAPIView):
    queryset = products.objects.all
    serializer_class = productscreateserializer

class ordersViewSet(viewsets.ModelViewSet):
        
    serializer_class = orderListSerializer
    queryset = orders.objects.all()


class UsersViewSet(viewsets.ModelViewSet):
    
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('-id')



class categoriesViewSet(viewsets.ModelViewSet):
    
    serializer_class = categoryserializer
    queryset = category.objects.all()


class  activeorders(ListAPIView):
    serializer_class=orderListSerializer
    def get_queryset(self):
        order=orders.objects.filter(ordered=False)
        return order    


class topproducts(ListAPIView):
   serializer_class=chartserializer
   def get(self,*args,**kwrgs):
        names=[]
        remove=[]
        od=order_details.objects.order_by('-quantity')
        
        for i in od:
           if i.product not in remove:
               remove.append(i.product)
           else:
                pass
        print(remove)
        for i in remove:
           names.append(i.name)   
           
        data={
            'label':names[:3],
        }    
        return Response(data)

class topusers(ListAPIView):
    serializer_class=UserSerializer
    def get_queryset(self):
        od=order_details.objects.order_by('user__username','quantity').distinct('user__username')
        names=[]
        for i in od :
        
           name=User.objects.all
           names.append(name)
        data={
            'label':names,
        }    
        return Response(data) 