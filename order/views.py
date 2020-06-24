from django.http import Http404
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from .models import orders, order_details, products, wishlistdetails, wishlist, review
from .serializers import orderListSerializer, orderdetails, reviewserializer
from user.models import User
from rest_framework.authtoken.models import Token
from products.models import features,productfeatures
import ast

class addtocart(APIView):
    def post(self, request):
        barcode = request.data.get('barcode', None)
        token = request.data.get('token', None)
        feats=request.data.get('features',[])
        print(barcode,token,feats)
        if barcode is None:
            return Response({"message": "invalid request"}, status=HTTP_400_BAD_REQUEST)
        if feats:    
            featrs=ast.literal_eval(feats)
        print(featrs)
        it = get_object_or_404(products, Barcode=barcode)
        order_ds= order_details.objects.filter(product=it, 
                                            user=Token.objects.get(key=token).user,
                                            ordered=False
                                                )

        features_count=features.objects.filter(product=it).count()
        if features_count>len(featrs):
            return Response({"message": "please Specify the Features"}, status=HTTP_400_BAD_REQUEST)
                    
        for i in featrs:
            print(i)
            order_ds=order_ds.filter(
                features__exact=i  
            )
        if order_ds.exists():
            order_item=order_ds.first()
            order_item.quantity+=1
            order_item.save()   
            print('dwqd')

            
        else:

            order_item= order_details.objects.create(product=it, 
                                            user=Token.objects.get(key=token).user,
                                            ordered=False
                                                )

            order_item.features.add(*featrs)
            order_item.save()
    
        order_qs = orders.objects.filter(user=Token.objects.get(key=token).user, ordered=False)
        if order_qs.exists():
            ord = order_qs[0]
            if not ord.items.filter(product__id=order_item.id).exists():
                    ord.items.add(order_item)
            return Response({"message": "this product is already in the cart"}, status=HTTP_200_OK)
                


        else:
            ord = orders.objects.create(user=Token.objects.get(key=token).user)
            ord.items.add(order_item)
            return Response({"message": "added successfully"}, status=HTTP_200_OK)

class deletefromcart(DestroyAPIView):
    permession_classes = [IsAuthenticated]
    queryset = order_details.objects.all()


class orderdetailsquantity(APIView):

    def post(self, request):
        token=request.data.get('token',None)
        print(token)
        use=Token.objects.get(key=token).user
        orderdetail_id = request.data.get('id', None)
        qty = request.data.get('quantity')
        if orderdetail_id is None:
            return Response({"message": "invalid request"}, status=Http404)
        cartorder = orders.objects.get(ordered=False, user=use)
        orderdetail = order_details.objects.get(user=use, ordered=False, id=orderdetail_id)
        orderdetail.quantity = qty
        orderdetail.save()
        cartorder.save()

        return Response({"message": "updated successfully"}, status=HTTP_200_OK)


class orderslist(ListAPIView):
   serializer_class = orderListSerializer

   def get_queryset(self):
        #print(self.request.META.get('HTTP_AUTHORIZATION',None))
        token=self.request.META.get('HTTP_AUTHORIZATION',None)
        use=Token.objects.get(key=token).user
        queryset = orders.objects.filter    (ordered=True, user=use)
        return queryset


class orderdetails(RetrieveAPIView):
    serializer_class = orderListSerializer

    def get_object(self):
        #print(self.request.META.get('HTTP_AUTHORIZATION',None))
        token=self.request.META.get('HTTP_AUTHORIZATION',None)
        use=Token.objects.get(key=token).user
        queryset = orders.objects.get(ordered=False, user=use)
        return queryset


'''
class addtowhitelist():
    def post(self,request):
        item_id=request.data.get('id',None)
        if item_id is None:
            return Response({"message":"invalid request"},status=Http404)
        it = get_object_or_404(branch_products, id=item_id)
        wish, created = wishlistdetails.objects.get_or_create(branch_products=it, use=request.user)
        wishs = wishlist.objects.filter(use=request.user)
        if wishs.exists():
            W = wishs[0]
            if W.items.filter(branch_products__id=it.id).exists():
                return Response({"message": "item already in the wishlist"}, status=Http404)
            else:
                W.items.add(wish)
                return Response(status=HTTP_200_OK)
        else:
            W = orders.objects.create(use=request.user)
            W.items.add(wish)
            return Response(status=HTTP_200_OK)
'''


class review(CreateAPIView):
    queryset = review.objects.all()
    serializer_class = reviewserializer


class topuserproducts(APIView):
    def get(self,request):
        token=request.META.get('HTTP_TOKEN',None)
        user=Token.objects.get(key=token).user
        user_orders=orders.objects.filter(user=user,ordered=True)
        products=[]
        counted=[]
        unique=[]
        dic={}
        for i in user_orders:
            for x in i.items.all():
                products.append(x.product.name)
        for i in products:
            if i in unique:
                pass
            else:
                unique.append(i)
        for i in unique:
            if products.count(i)>2:
                pass
            else:
               dic={
                   'name':i,
                   'count':products.count(i)
               }    

               counted.append(dic)

        print(sorted(counted, key = lambda i: i['count'],reverse=True)[:2]  )

        return Response( sorted(counted, key = lambda i: i['count'],reverse=True)[:2] )

class submitorder(APIView):
    def post(self,request):
        token=request.data.get('token',None)
        order_id=request.data.get('order_id',None)
        points_req=request.data.get('points',None)
        use=Token.objects.get(key=token).user
        ord=orders.objects.get(user=use,ordered=False)  
        print(token,points_req,ord.total())

        if(int(points_req) <= 0):
            if( ord.total() >=1  and  ord.total() <=200  ):
                  pts = (ord.total()*5)/100
                  point=int(pts)
                  use.points+=point
                  ord.ordered=True
                  for i in ord.items.all():
                      i.ordered=True
                      i.save()
                  use.save()
                  ord.save()
                  return Response(status=HTTP_200_OK)

            elif(ord.total() > 200 and ord.total() <=1000):
                  pts = (ord.total()*15)/100
                  point=int(pts)
                  use.points+=pts
                  ord.ordered=True
                  for i in ord.items.all():
                      i.ordered=True
                      i.save()
                  use.save()
                  ord.save()
                  return Response(status=HTTP_200_OK)

            elif(ord.total() >1000 and ord.total() <=5000):
            
                  pts = (ord.total()*20)/100
                  point=int(pts)
                  use.points+=pts
                  ord.ordered=True
                  for i in ord.items.all():
                      i.ordered=True
                      i.save()
                  use.save()
                  ord.save()
                  return Response(status=HTTP_200_OK)

            elif(ord.total() > 5000 ):
                  
                  pts = (ord.total()*25)/100
                  point=int(pts)
                  use.points+=pts
                  ord.ordered=True          
                  for i in ord.items.all():
                      i.ordered=True
                      i.save()
                  use.save()
                  ord.save() 
                  return Response(status=HTTP_200_OK)

                  
        else: 
            use.points-=int(points_req)
            ord.final_order_price=ord.total()-float(int(points_req)/4)
            ord.ordered=True
            use.save()
            ord.save()
            for i in ord.items.all():   
                      i.ordered=True
                      i.save()
            return Response(status=HTTP_200_OK)