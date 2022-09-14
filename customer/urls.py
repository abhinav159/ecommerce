from django.urls import path
from . import views

urlpatterns=[
    path('customerhome',views.customerhome),
    path('productdetails',views.productdetails),
    path('viewcart',views.viewcart),
    path('myorders',views.myorders),
    path('changepassword',views.changepassword),
    path('name',views.name),
]