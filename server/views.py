from django.shortcuts import render

# Create your views here.
def approveseller(request):
    return render(request,'servertemplates/approveseller.html')
def home(request):
    return render(request,'servertemplates/home.html')
def login(request):
    return render(request,'servertemplates/login.html')
def viewcustomer(request):
    return render(request,'servertemplates/viewcustomer.html')
def viewseller(request):
    return render(request,'servertemplates/viewseller.html')
def viewsellerorder(request):
    return render(request,'servertemplates/viewsellerorder.html')
