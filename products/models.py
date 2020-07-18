from django.db import models

def CreateQR_Code(name):
    qr=name.replace(' ','_')
    last=qr.upper()
    return f'{last}_BRANCH'

class category(models.Model):
    name=models.CharField(unique=True,max_length=30)
    def __str__(self):
        return self.name

class brand_name(models.Model):
   name=models.CharField(unique=True,max_length=20)
   def __str__(self):
       return self.name

class branch(models.Model):
    name=models.CharField(max_length=100 ,default='',unique=True)
    QR_code = models.CharField(max_length=233,default='QR CODE WILL BE GENERATED AUTOMATICALLY')

    def __str__(self):
        return self.name

    def save(self,*args,**kwrgs):
        self.QR_code=CreateQR_Code(self.name)
        super(branch,self).save(*args,**kwrgs)
  


class products(models.Model):
    name=models.CharField(max_length=100)
    Barcode=models.CharField(max_length=100,unique=True)
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    description=models.TextField()
    price=models.FloatField(default=100.0)
    discount_price=models.FloatField(default=0.00)
    image=models.ImageField(default='')
    branch=models.ForeignKey(branch,on_delete=models.CASCADE)
    brands=models.ForeignKey(brand_name,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return f'{self.name}_{self.branch}'
    class Meta:
            unique_together=(
            ('name','branch')
        )

 
class features(models.Model):
    product=models.ForeignKey(products,on_delete=models.CASCADE)
    featurename=models.CharField(max_length=100)
    class Meta:
        unique_together=(
            ('product','featurename')
        )
    def __str__(self):
        return self.featurename

class productfeatures(models.Model):
    feat=models.ForeignKey(features,on_delete=models.CASCADE)
    values=models.CharField(max_length=100)
    class Meta:
        unique_together=(
            ('feat','values')
        )
    def __str__(self):
        return self.values


class limited_offers(models.Model):
    product=models.ForeignKey(products,on_delete=models.CASCADE)
    new_price=models.FloatField(default=0.00)
    start_date=models.DateTimeField(auto_now_add=True)
    end_date=models.DateTimeField()
