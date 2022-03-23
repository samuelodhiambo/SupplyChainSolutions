from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(
        blank=False,
        null=False,
        max_length=50
    )
    description = models.CharField(
        blank=False,
        null=False,
        max_length=250
    )
    quantity = models.IntegerField(
        blank=False,
        null=False,
    )
    price = models.IntegerField(
        blank=False,
        null=False,
    )
    info = models.CharField(
        blank=True,
        null=True,
        max_length=500
    )
    pimage = models.ImageField(
        upload_to='images',
        null=True,
        blank = True,
        editable=True
    )

    class Meta:
        db_table = 'Product'

    def __str__(self) -> str:
        return self.product_name


