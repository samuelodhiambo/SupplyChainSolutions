from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from product.models import Product
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required

# Create your views here.
def addToCartView(request):
    return render(request)

def showCartView(request, template="showCart.html"):
    orders = Order.objects.filter(user=request.user.id)
    order = Order()
    if request.method == 'POST':
        pk = request.POST.get('pk')
        print("=====", pk)
        if not Order.objects.filter(user=request.user, product=pk).exists():
            print("=======", 'ian') 
            product = Product.objects.get(id=pk)
            order.user = request.user
            order.order_amount = request.POST.get('order_amount')
            order.product = product
            print("=================", order)
            try:
                order.save()
                return redirect('showCart')
            except Exception as e:
                error = e + 'Order Failed!!!'
                print(error)
                context = {
                    'orders': orders,
                    'error': error
                }
                return render(request, template, context)
        error = 'You have already placed that order'
        context = {
            'orders': orders,
            'error': error
        }
        return render(request, template, context)
    return render(request, template, {'orders': orders})

def ajaxAddCart(request):
    if request.method == "POST":
        # get the form data
        id = request.POST.get('id')
        order = get_object_or_404(Order, id=id)
        order.order_amount = request.POST.get('order_amount')
        # save the data and after fetch the object in instance
        try:
            order.save()
            print("Iannnnnnnnnnnnnnnnnnnnn")
            instance = Order.objects.get(id=id)
            # product = Order.objects.filter(id=input.product)
            # serialize in new object in json
            total = (instance.product.price * instance.order_amount)
            print(total)
            order = {
                'id': instance.id,
                'product': {
                    'product_name': instance.product.product_name,
                    'pimage': instance.product.pimage.url
                },
                'order_amount': instance.order_amount,
                'total': total
            }
            print(total)
            ser_instance = order
            # ser_instance = serializers.serialize('json', [ instance, ])
            print(ser_instance) 
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        except Exception as e:
            # some form errors occured.
            return JsonResponse({"error": "failed to update amount"}, status=400)

def deleteOrder(request, id):
    order = get_object_or_404(Order, id=id)
    if request.method == 'POST':
        if order.user == request.user:
            order.delete()
            return redirect('showCart')
        return redirect('showCart')
    return redirect('showCart')
