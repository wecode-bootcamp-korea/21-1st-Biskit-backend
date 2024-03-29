from django.db import models

class Status(models.Model):
    status = models.CharField(max_length=45)

    class Meta:
        db_table = 'status'

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user       = models.ForeignKey('users.User', on_delete=models.CASCADE)
    status     = models.ForeignKey(Status, on_delete=models.CASCADE)

    class Meta:
        db_table = 'orders'

class OrderItem(models.Model):
    quantity    = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    product     = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    order       = models.ForeignKey(Order, on_delete=models.CASCADE)

    class Meta:
        db_table = 'order_items'

class DeliveryDate(models.Model):
    date       = models.CharField(max_length=4)
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'delivery_dates'
