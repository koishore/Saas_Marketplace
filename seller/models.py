from django.db import models
from core.models import CustomUser as User


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    image = models.URLField(max_length=200, default = 'https://via.placeholder.com/150')
    price = models.FloatField(default=0)
    inventory = models.PositiveIntegerField(default=0)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.product_name
