from django.db import models
import qrcode
import random
class category(models.Model):
    name=models.CharField(unique=True,max_length=30)

    def __str__(self):
        return self.name

class products(models.Model):
    name=models.CharField(max_length=50)
    price=models.FloatField(default=100.0)
    Barcode=models.CharField(max_length=50)
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    description=models.TextField()
    image=models.ImageField(upload_to='pics',default='')
    def __str__(self):
        return self.name


class branch(models.Model):
    QR_code = models.CharField(max_length=233)

    def __str__(self):
        return self.QR_code


class branch_products(models.Model):
    product=models.ForeignKey(products,on_delete=models.CASCADE)
    branch=models.ForeignKey(branch,on_delete=models.CASCADE,related_name='br')
    price = models.FloatField(null=True)
    prev_price = models.FloatField(blank=True, null=True)
    quantity=models.IntegerField()
