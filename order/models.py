from django.db import models
from user.models import User
from products.models import products,branch_products
from GP_FINAL import settings

class order_details(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True)
    ordered=models.BooleanField(default=False)
    product=models.ForeignKey(products,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    def price(self):
        return self.product.price * self.quantity



class orders(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    ordered=models.BooleanField(default=False)
    items=models.ManyToManyField(order_details)
    def total(self):
        tot=0
        for item in self.items.all():
            tot+=item.price()
        return tot
    

class wishlistdetails(models.Model):
    product = models.ForeignKey(branch_products, on_delete=models.CASCADE)

class wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(wishlistdetails)

class review(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body=models.CharField(max_length=250)

'''
class order_history(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.FloatField()

class order_details_history(models.Model):
    order_id=models.ForeignKey(order_history,on_delete=models.CASCADE)
    product=models.ForeignKey(products,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    price=models.FloatField()
'''