from django.db import models
from product.models import Product
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Delivered', 'Delivered'),
    )
    order_amount = models.IntegerField(null=True, blank=True, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True, null=True)
    time_ordered = models.TimeField(auto_now_add=True, null=True, blank=True)
    status = models.CharField(choices=STATUS, max_length=200, null=True, default='Pending')

    class Meta:
        db_table = 'Order'

    def __str__(self) -> str:
        return self.product.product_name

    @property
    def total(self):
        return self.order_amount * self.product.price
