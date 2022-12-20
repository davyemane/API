from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    
    @property
    def get_discount(self):
        return "%.2f"%(float(self.price) * 0.5)
# Create your models here.

    def __str__(self):
        return self.name