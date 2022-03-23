from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def addView(request, template="product.html"):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = Product()
            product.user = request.user
            product.product_name = form.cleaned_data['product_name']
            product.description = form.cleaned_data['description']
            product.quantity = form.cleaned_data['quantity']
            product.price = form.cleaned_data['price']
            product.info = form.cleaned_data['info']
            product.pimage = request.FILES.get('pimage')
            try:
                product.save()
                return redirect('home')
            except Exception as e:
                context = {
                    'form': form,
                    'error': e,
                }
                return render(request, template, context)
        else:
            form = ProductForm(request.POST)
            return render(request, template, {'form': form})
    form = ProductForm()
    context = {'form': form}
    return render(request, template, context)
