
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/',include('customer.urls')),
    path('seller/',include('seller.urls')),
    path('common/',include('common.urls')),
    path('server/',include('server.urls'))
]
