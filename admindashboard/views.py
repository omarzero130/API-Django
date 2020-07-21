from django.shortcuts import render
from products.models import products,category,branch,features,productfeatures,limited_offers,brand_name
from user.models import User
from order.models import orders,order_details,wishlist,wishlistdetails,review
from order.serializers import orderListSerializer,orderdetails
from rest_framework import viewsets
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,RetrieveUpdateAPIView
from products.serializers import (productsserializer,categoryserializer,productscreateserializer,branchserializer,
                                 FeatureValuesSerializer,brandserializer,ProductFeaturesSerializer)
from order.serializers import chartserializer
from user.serializers import UserSerializer
from rest_framework.response import Response
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework import filters,pagination
from rest_framework.status import HTTP_200_OK


class productpagination(pagination.PageNumberPagination):
    page_size=10
    pag_size_query_param='size'
    max_page_size=20
    def get_paginated_response(self,data):
        queryset={
            'next':self.get_next_link(),
            'prev':self.get_previous_link(),
            'count':self.page.paginator.count,
            'results':data
        }
        return Response(queryset)

class productslist(ListAPIView):
    queryset = products.objects.all().order_by('-id')
    serializer_class = productsserializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['Barcode','name']


class singleproduct(RetrieveAPIView):
    queryset = products.objects.all()
    serializer_class = productsserializer   

class productsdelete(DestroyAPIView):
    queryset = products.objects.all()
    serializer_class = productsserializer  
class productscreate(CreateAPIView):
    queryset = products.objects.all
    serializer_class = productscreateserializer

class productsupdate(UpdateAPIView):
    queryset = products.objects.all()
    print('h5a')

    serializer_class = productsserializer


class branchViewSet(viewsets.ModelViewSet):
    queryset=branch.objects.all().order_by('-id')
    serializer_class=branchserializer

class orderedList(ListAPIView):
        
    serializer_class = orderListSerializer
    queryset = orders.objects.filter(ordered=True)



class activeList(ListAPIView):
        
    serializer_class = orderListSerializer
    queryset = orders.objects.filter(ordered=False)


class activeEdit(APIView):
    def post(self,request):
        order_id=request.data.get('id',None)
        print(order_id)
        if order_id is not None:
            order_qs=orders.objects.get(id=order_id)
            if(order_qs.ordered):
                order_qs.ordered =False
                order_qs.save()
            else:
                order_qs.ordered =True
                order_qs.save()
        return Response({'message':'order updated successfully'})    

class singleorder(RetrieveAPIView):
    serializer_class=orderListSerializer
    queryset=orders.objects.all()

class UsersViewSet(viewsets.ModelViewSet):
    
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('-id')



class BrandsViewSet(viewsets.ModelViewSet):
    
    serializer_class = brandserializer
    queryset = brand_name.objects.all().order_by('-id')


class UserUpdate(APIView):
    def post(self,request):
        user_id=request.data.get('id', None)
        if user_id :
            user=User.objects.get(id=user_id)
            if(user.is_superuser):
                user.is_staff = False
                user.is_superuser= False
                user.save()
            else:
                user.is_staff = True
                user.is_superuser= True
                user.save()
            return Response({'message':'added successfully'})
        else:
            return Response({'message':'Failed'})
        



class categoriesViewSet(viewsets.ModelViewSet):
    filter_backends=[filters.SearchFilter]
    search_fields = ['name']
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
        productlist=[]
     
        od=order_details.objects.filter(ordered=True).values('product').distinct()
        
        
        for i in od:
            prod=products.objects.get(id=i['product'])
            qty=order_details.objects.filter(product__id=i['product'],ordered=True).aggregate(Sum('quantity'))['quantity__sum']
            dict={} 
            dict['name']=prod.name
            dict['qty']=qty
            productlist.append(dict)
             
        data={
            'label':productlist,
        }    
        print(data)
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
        

class Userstats(ListAPIView):
    serializer_class=UserSerializer
    def get(self,request,*args,**kwrgs):
        users=User.objects.all().count()

        return Response(users)

class Orderstats(ListAPIView):
    serializer_class=orderListSerializer
    def get(self,request,*args,**kwrgs):
        order=orders.objects.filter(ordered=True).count()

        return Response(order)

class Productstats(ListAPIView):
    serializer_class=productsserializer
    def get(self,request,*args,**kwrgs):
        product=products.objects.all().count()

        return Response(product)        


class GetUserOrders(ListAPIView):
    serializer_class=orderListSerializer
    def get_queryset(self):
        userid=self.request.META.get('HTTP_USERID',None)        
        print(userid)
        queryset=orders.objects.filter(user=userid)
        return queryset


class productfeatureslist(ListAPIView):
    serializer_class=ProductFeaturesSerializer
    queryset=features.objects.all()        

class addfeatures(APIView):
    def post(self,request,*args,**kwrgs):
        product=self.request.data.get('product',None)
        featurename=self.request.data.get('featurename',None)
        values=self.request.data.get('values',None)
        print(self.request.data)
        prod=products.objects.get(id=product)
        feat=features.objects.create(featurename=featurename,product=prod)
        for i in values:
           featurevalues=productfeatures.objects.create(feat=feat,values=i)
           featurevalues.save()
        feat.save()
        return Response({'message':'ok added'})

class singlefeature(RetrieveAPIView):
    serializer_class=ProductFeaturesSerializer
    queryset=features.objects.all()


class deletefeatures(DestroyAPIView):
    serializer_class=ProductFeaturesSerializer
    queryset=features.objects.all()

class deletefeaturesvalues(DestroyAPIView):
    serializer_class=FeatureValuesSerializer
    queryset=productfeatures.objects.all()

class featurevaluesUpdate(UpdateAPIView):
    serializer_class=FeatureValuesSerializer
    queryset=productfeatures.objects.all()


class productfeaturesUpdate(UpdateAPIView):
    serializer_class=ProductFeaturesSerializer
    queryset=features.objects.all()        


class offers_create(APIView):
    def post(self,request):
        product= request.data.get('product', None)
        price=request.data.get('new_price',None)
        ends_at=request.data.get('ends_at',None)
        prod=products.objects.get(id=product)
        prod.discount_price = price
        prod.save()
        offer=limited_offers.objects.create(product=prod,new_price=price,end_date=ends_at)
        return Response({'message':"added"}, status=HTTP_200_OK)
