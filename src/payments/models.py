from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=8,decimal_places=2)

    def __str__(self):
        return self.name
