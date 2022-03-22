from django.shortcuts import render

# Create your views here.
def addView(request, template="product.html"):
    context = {}
    return render(request, template, context)
