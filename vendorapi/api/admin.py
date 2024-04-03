from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Vendor, PurchaseOrder, HistoricalPerformance

admin.site.register(Vendor)
admin.site.register(PurchaseOrder)
admin.site.register(HistoricalPerformance)