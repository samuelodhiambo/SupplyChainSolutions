from django.shortcuts import render

# Create your views here.
def homeView(request, template="home.html"):
    context = {}
    return render(request, template, context)