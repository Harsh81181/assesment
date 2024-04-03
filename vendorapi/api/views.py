# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from .serializers import VendorSerializer, PurchaseOrderSerializer, HistoricalPerformanceSerializer

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    
    #api/vendors/{vendor_id}/performance
    @action(detail=True,methods=['get'])
    def performance(self, request,pk=None):
        try:
            vendor=Vendor.objects.get(pk=pk)
            perf=PurchaseOrder.objects.filter(vendor=vendor)
            perf_serializer=PurchaseOrderSerializer(perf,many=True,context={'request':request})
            return Response(perf_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'Performance has not found'
            })

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
