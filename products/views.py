from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .models import products,branch,category,limited_offers,productfeatures,features,brand_name
from .serializers import (productsserializer,
                          productscreateserializer,
                          branchserializer,categoryserializer)
from rest_framework import filters
from rest_framework.views import APIView
import requests
import urllib.request 
import bs4 
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
import ast
from django.db.models import Q
from itertools import chain



class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 2

class productslist(ListAPIView):
   serializer_class = productsserializer
   def get_queryset(self):
        brs= self.request.headers['Branch']
        br=branch.objects.get(QR_code=brs)
        queryset = products.objects.filter(branch=br)
        barcode = self.request.query_params.get('barcode', None)
        if barcode is not None:
            queryset=products.objects.filter(Barcode=barcode)
            print(queryset)
        return queryset

class productscreate(CreateAPIView):
    queryset = products.objects.all()
    serializer_class = productscreateserializer




class branchviewset(ModelViewSet):
    serializer_class = branchserializer
    queryset = branch.objects.all()


class categoryviewset(ModelViewSet):
    serializer_class = categoryserializer
    queryset = category.objects.all().order_by('-id')

class productfilter(ListAPIView):
    serializer_class=productsserializer
    def get_queryset(self):
        ids=self.request.query_params.get('id', None)
        print(ids)
        cat=category.objects.get(id=ids)
        prod=products.objects.filter(category=cat)
        return prod

class homepage(ListAPIView):
    serializer_class=productsserializer
    def get_queryset(self):
        l=[]
        c=[]
        brands=[]
        cat=self.request.META.get('HTTP_CATEGORY',[])
        max=self.request.META.get('HTTP_MAX',None)
        min=self.request.META.get('HTTP_MIN',None)
        brand=self.request.META.get('HTTP_BRAND1',[])
        feats=self.request.META.get('HTTP_FEATS',[])
        name = self.request.query_params.get('name', None)

        if feats:    
            feats=ast.literal_eval(feats)
        if cat:
            cat=ast.literal_eval(cat)
        if brand:
            brand=ast.literal_eval(brand)    
        queryset=products.objects.all()
        print(max)
        if name:
            queryset=queryset.filter(Q(name__icontains=name))
        if(cat):
            for i in cat:
                categ=category.objects.get(name=i)
                c.append(categ.id)
                
            queryset=queryset.filter(category__in=c)

        if(max and min):
                queryset=queryset.filter(price__lte=max,price__gte=min)
        if(brand):
            for i in brand: 
                br=brand_name.objects.get(name=i)
            print(brands)
    
            queryset=queryset.filter(brands__in=brands)    
        if(feats):
            for i  in feats:
               if(productfeatures.objects.filter(values=i).count()>0): 
                    PF=productfeatures.objects.filter(values=i)
                    for x in PF:
                        F=features.objects.get(id=x.feat.id)
                        print(F.product.id)
                        l.append(F.product)
                    for x in queryset:
                        if x not in l:
                            queryset=queryset.exclude(id = x.id)
               else:
                   pass
        return queryset
   


class homepage2(APIView):
    def get(self,request):
        categorys=[]
        branches=[]
        features=[]
        brs=branch.objects.all()
        for i in brs:
            branches.append(i.name)
        cats=category.objects.all()    
        for i in cats:
            categorys.append(i.name)    

        data={
            'categories':categorys,
            'branches':branches
        }    
        return Response(data)
def scrape():
    path=''
    counter=5

    session= requests.Session()
    session.headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
    }
    url='https://egypt.souq.com/eg-en/samsung/mobile-phones-33%7Csmart-watches-511%7Ctablets-94%7Cfitness-technology-498%7Cpower-banks-562/samsung/a-t-7/s/?_=1500309575629&sortby=sr&page=1&ref=nav'
    content=session.get(url,verify=False).content
    soup=bs4.BeautifulSoup(content,'html.parser')
    result=soup.find_all('div',{'class':'column column-block block-list-large single-item'})
    for i in result:
        counter+=1
        name=i.find_all('h1',{'class':'itemTitle'})[0]
        price=i.find('h3',{'class':'itemPrice'}).text
        price2=price[0:len(price)-3]
        print(price2)
        str=price2.replace(' ','')
        str2=str.replace(',','')
        finalprice=float(str2)
        image=i.find('img',{'class':'img-size-medium imageUrl'})['data-src']
        path=f'pics/{counter}.jpg'
        img=f'{counter}.jpg'
        barcode=f'name{counter}'
        description='this is my product'
        urllib.request.urlretrieve(image,path)
        cat=category.objects.get(id=1)
        br=branch.objects.get(id=1)
        products.objects.create(name=name.text,Barcode=barcode,branch=br,image=img,
        description=description,price=finalprice,category=cat)

#scrape();
