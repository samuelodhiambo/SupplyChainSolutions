from django.shortcuts import render
from product.models import Product

# Create your views here.
def homeView(request, template="home.html"):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, template, context)