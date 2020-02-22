from django.http import Http404
from rest_framework import status
from rest_framework.generics import CreateAPIView,ListAPIView,DestroyAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from .models import orders,order_details,products,wishlistdetails,wishlist,review
from .serializers import orderListSerializer,orderdetails,reviewserializer
from user.models import User
from rest_framework.authtoken.models import Token





class addtocart(APIView):
    def post(self,request):
        item_id= request.data.get('id',None)
        token=request.data.get('token',None)
        print(token)
        if item_id is None:
            return Response({"message":"invalid request"},status=Http404)

        it = get_object_or_404(products, id=item_id)
        print("1")
        order_ds, created = order_details.objects.get_or_create(product=it, user=Token.objects.get(key=token).user, ordered=False)
        print("2")
        order_qs = orders.objects.filter(user=Token.objects.get(key=token).user, ordered=False)
        print("3")
        if order_qs.exists():
            print("4")
            ord = order_qs[0]
            print(ord.total())
            if ord.items.filter(product__id=it.id).exists():
                print("6")
                order_ds.quantity += 1
                order_ds.save()
                return Response({"message":"this product is already in the cart"},status=HTTP_200_OK)
            else:
                ord.items.add(order_ds)
                return Response({"message":"added successfully"},status=HTTP_200_OK)

        else:
            print('sdfgh')
            ord = orders.objects.create(user=Token.objects.get(key=token).user)
            ord.items.add(order_ds)
            return Response({"message":"added successfully"},status=HTTP_200_OK)




class deletefromcart(DestroyAPIView):
    permession_classes=[IsAuthenticated]
    queryset=order_details.objects.all()



class orderdetailsquantity(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        orderdetail_id=request.data.get('id',None)
        qty=request.data.get('quantity')
        if orderdetail_id is None:
            return Response({"message":"invalid request"},status=Http404)
        cartorder=orders.objects.get(ordered=False,user=request.user)   
        orderdetail=order_details.objects.get(user=request.user,ordered=False,id=orderdetail_id)
        orderdetail.quantity=qty
        orderdetail.save()
        cartorder.save()
        
        return Response({"message":"updated successfully"},status=HTTP_200_OK)

class orderslist(ListAPIView):
    serializer_class = orderListSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset=orders.objects.filter(ordered=True,user=self.request.user)
        return queryset


class orderdetails(RetrieveAPIView):
    serializer_class = orderListSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        queryset = orders.objects.get(ordered=False, user=self.request.user)
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
