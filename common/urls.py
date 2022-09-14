from django.urls import path
from . import views


urlpatterns=[
    path('inddex_a/',views.inddex_a),
    path('seller_login/',views.seller_login),
    path('customerlogin',views.customerlogin),
    path('sellersignup',views.sellersignup),
    path('customersignup',views.customersignup),
    path('changepassword',views.changepassword)
]