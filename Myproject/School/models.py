from django.db import models

class Shoes(models.Model):
    name = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)
    desc = models.TextField()
    prize = models.IntegerField()
    image = models.ImageField(upload_to="post_images/", null=True, blank=True)
