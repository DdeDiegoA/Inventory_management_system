from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100, unique=True)
    description=models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural="Categories"

class Product(models.Model):
    name=models.CharField(max_length=200)
    cod=models.CharField(max_length=50,unique=True)
    category=models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='products'
    )
    buy_price=models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    sell_price=models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )

    def __str__(self):
        return f"{self.name} ({self.cod})"

class Inventory(models.Model):
    product=models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name='inventary'
    )
    stock=models.PositiveIntegerField(default=0)
    min_stock=models.PositiveIntegerField(default=10)

    def __str__(self):
        return f"Stock de {self.product.name}"
    
    class Meta:
        verbose_name_plural= 'Inventories'