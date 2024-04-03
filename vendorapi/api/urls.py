from django.contrib import admin
from django.urls import path,include
from api.views import VendorViewSet,PurchaseOrderViewSet
from rest_framework import routers


router=routers.DefaultRouter()
router.register(r'vendors',VendorViewSet) 
router.register(r'purchaseOrder',PurchaseOrderViewSet)

urlpatterns = [
    path('' ,include(router.urls)),
]