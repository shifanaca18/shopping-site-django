from django.db import models

class Product(models.Model):
    item=models.CharField(max_length=50)
    price=models.CharField(max_length=20)
    image=models.ImageField(upload_to='images/', blank=True)
    desc=models.TextField(max_length=500)
    def __str__(self):
        return self.item