from django.db import models

# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=20, primary_key=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def calculate_average_response_time(self, acknowledgment_date):
        # Calculate the average response time for the vendor
        # Get all completed purchase orders for the vendor
        completed_orders = PurchaseOrder.objects.filter(
            vendor=self,
            status='completed',
            acknowledgment_date__isnull=False
        )

        # Calculate the time difference for each completed order
        response_times = [(order.acknowledgment_date - order.issue_date).total_seconds() for order in completed_orders]

        # Calculate the average response time
        if response_times:
            average_response_time = sum(response_times) / len(response_times)
        else:
            average_response_time = 0.0

        # Update the vendor's average_response_time field
        self.average_response_time = average_response_time
        self.save()

    def __str__(self):
        return self.name

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=255, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, default='pending')
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"PO-{self.po_number} for {self.vendor.name}"

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)
    
    

    def __str__(self):
        return f"Performance for {self.vendor.name} on {self.date}"