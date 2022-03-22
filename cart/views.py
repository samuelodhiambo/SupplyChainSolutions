from django.shortcuts import render

# Create your views here.
def addToCartView(request):
    return render(request)

def showCartView(request, template="showCart.html"):
    context = {}
    return render(request, template, context)
