from django.shortcuts import render,get_object_or_404
from decimal import Decimal
from django.conf import settings
from django.urls import reverse 
from paypal.standard.forms import PayPalPaymentsForm 
from order.models import orders
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def payment_done(request):
    order=get_object_or_404(orders,user=request.user,ordered=False)
    print(order.ordered)
    order.ordered = True
    order.save()
    print(order.ordered)

    return render(request,'done.html')


@csrf_exempt
def payment_canceled(request):
    return render(request,'done.html')


def checkout(request):
    order=get_object_or_404(orders,user=request.user,ordered=False)
    host=request.get_host()

    paypal_dict={
        'business':settings.PAYPAL_RECIVER_EMAIL,
        'amount':'%.2f' %order.total(),
        'item_name':f'Order {order.id}',
        'invoice':str(order.id),
        'currency_code':'USD',
        'notify_url':'http://{}{}'.format(host,reverse('paypal-ipn')),
        'return_url':'http://{}{}'.format(host,reverse('payment:done')),
        'cancel_return': 'http://{}{}'.format(host,reverse('payment:canceled')),
    }
    form=PayPalPaymentsForm(initial=paypal_dict)
    return render(request,'checkout.html',{'order':order,'form':form})