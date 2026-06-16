from django.db import models


class Category(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='products'
    )
    full_name = models.CharField(max_length=200)
    fabric = models.CharField(max_length=200, blank=True)
    style = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rating = models.FloatField(default=5.0)

    # Для SuitSVG
    color = models.CharField(max_length=20, default='#1a1a2e')        # основной цвет
    accent = models.CharField(max_length=20, default='#d4af37')       # цвет акцента (золото)
    pattern = models.CharField(max_length=50, default='solid')        # solid / stripes / checks
    tag = models.CharField(max_length=50, blank=True)                  # «Хит», «Новинка»

    image = models.ImageField(upload_to='products/', blank=True, null=True)
    stock = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name