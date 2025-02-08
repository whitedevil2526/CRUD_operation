from django.db import models

class Shoes(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100, default=None) 
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    desc = models.TextField()
    image = models.ImageField(upload_to='shoe_images/', blank=True, null=True)

    def __str__(self):
        return self.name


