from django.db import models

# Create your models here.
class CheckItems(models.Model):
    ignore_empty = models.BooleanField()

class Item(models.Model):
    title = models.TextField()
    price = models.IntegerField()
    inventory_count = models.IntegerField()
    genre = models.TextField()


class Purchase(models.Model):
    item = models.ForeignKey('products.Item', related_name='purchases', on_delete=models.CASCADE, null=True, )
