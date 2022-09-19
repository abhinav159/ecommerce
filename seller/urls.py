from django.urls import path
from . import views


urlpatterns=[
    path('sellerhome/',views.seller_home),
    path('cart/',views.cart),
    path('myorder/',views.myorder),
    path('addproduct/',views.addproduct),
    path('changepassword/',views.changepassword),
    path('updatestock/',views.updatestock),
    path('image/',views.image)
]