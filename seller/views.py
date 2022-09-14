from django.shortcuts import render

def seller_home(request):
    return render(request,'sellertemplates/sellerhome.html')

# Create your views here.
def cart(request):
    return render(request,'sellertemplates/cart.html')
def myorder(request):
    return render(request,'sellertemplates/myorder.html')
def addproduct(request):
    return render(request,'sellertemplates/addproduct.html')  
def changepassword(request):
    return render(request,'sellertemplates/changepassword.html')  
def updatestock(request):
    return render(request,'sellertemplates/updatestock.html')    