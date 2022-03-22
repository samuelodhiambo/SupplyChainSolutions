from django.shortcuts import render

# Create your views here.
def loginView(request, template="login.html"):
    context = {}
    return render(request, template, context)

def registerView(request, template="signup.html"):
    context = {}
    return render(request, template, context)

def logoutView(request):
    return render(request)
