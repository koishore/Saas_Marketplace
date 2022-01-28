from django.db import models
from core.models import CustomUser as User
from seller.models import Product

class Cart(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    def __str__(self):
        return "{}_{}".format(self.buyer.email, self.product.product_name)

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    address = models.CharField(max_length = 250)
    is_shipped = models.BooleanField(default=False)
    is_out_for_delivey = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)
