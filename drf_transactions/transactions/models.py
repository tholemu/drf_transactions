from django.db import models


class Transaction(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.DecimalField(max_digits=16, decimal_places=8)
    order_price = models.DecimalField(max_digits=17, decimal_places=2,blank=True)

    class Meta:
        ordering = ['created']
