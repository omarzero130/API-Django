from django.db import models
import qrcode
import random
class category(models.Model):
    name=models.CharField(unique=True,max_length=30)

    def __str__(self):
        return self.name


class branch(models.Model):
    name=models.CharField(max_length=100)
    QR_code = models.CharField(max_length=233)

    def __str__(self):
        return self.QR_code


class products(models.Model):
    name=models.CharField(max_length=50)
    price=models.FloatField(default=100.0)
    Barcode=models.CharField(max_length=50)
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    description=models.TextField()
    image=models.ImageField(upload_to='pics',default='')
    branch=models.ForeignKey(branch,on_delete=models.CASCADE)
    def __str__(self):
        return self.name


