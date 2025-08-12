from django.db import models

# Create your models here.

from django.db import models

# Each category represents a "corner" in the boutique (e.g., Perfumes, Essences)
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    # qr_code_id = models.CharField(max_length=100, unique=True)  # To map QR codes to corners

    def __str__(self):
        return self.name


# Products linked to a specific Category
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name


# Temporary cart model (if you're not using a login system)
class CartItem(models.Model):
    session_id = models.CharField(max_length=255)  # track user without login
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def get_total_price(self):
        return self.quantity * self.product.price


# This will represent a confirmed order before redirecting to WhatsApp
class Order(models.Model):
    session_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=20)

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def get_total_price(self):
        return self.quantity * self.price
