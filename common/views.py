from django.shortcuts import render

def inddex_a(request):
    return render(request,'commontemplates/inddex_a.html')
def seller_login(request):
    return render(request,'commontemplates/seller_login.html')
def customerlogin(request):
    return render(request,'commontemplates/customerlogin.html')
def sellersignup(request):
    return render(request,'commontemplates/sellersignup.html')
def customersignup(request):
    return render(request,'commontemplates/customersignup.html')
def changepassword(request):
    return render(request,'commontemplates/changepassword.html')