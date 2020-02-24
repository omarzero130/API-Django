from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .models import products,branch_products,branch,category
from .serializers import (productsserializer,
                          productscreateserializer,categoryserializer)
from rest_framework import filters

class productslist(ListAPIView):
    br= request.query_params.get('branch')
    queryset = products.objects.filter(branch=br)
    serializer_class = productsserializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['Barcode','name']

class productsdelete(RetrieveDestroyAPIView):
    queryset = products.objects.all()
    serializer_class = productsserializer
  

class productscreate(CreateAPIView):
    queryset = products.objects.all
    serializer_class = productscreateserializer



class productfilter(ListAPIView):
    serializer_class=productsserializer
    def get_queryset(self):
        ids=self.request.query_params.get('id', None)
        print(ids)
        cat=category.objects.get(id=ids)
        prod=products.objects.filter(category=cat)
        return prod



'''
class productbranchcreate(CreateAPIView):
    serializer_class = productbranchcreateSerializer
    queryset = branch_products.objects.all()



class branchviewset(ModelViewSet):
    serializer_class = branchserializer
    queryset = branch.objects.all()
'''

class categoryviewset(ModelViewSet):
    serializer_class = categoryserializer
    queryset = category.objects.all().order_by('-id')
