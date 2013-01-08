          # -*- coding: utf-8 -*-
from django.db import models
from catalog.models import Product

class CartProduct(models.Model):
    cartitem = models.ForeignKey('CartItem')
    product = models.ForeignKey(Product, verbose_name='Товар')
    quantity = models.IntegerField(default=1, verbose_name='Количество')

class CartItem(models.Model):
    cart_id = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    product = models.ManyToManyField(Product, through=CartProduct)

    class Meta:
        db_table = 'cart_item'

class Client(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField()
    address = models.CharField(max_length=500, null=True, blank=True, verbose_name="Адрес")
    cart = models.ForeignKey(CartItem)
    ordered_at = models.DateTimeField(auto_now_add=True )
    subtotal = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2, verbose_name="Сумма")
    referrer = models.URLField(verify_exists=False, max_length=500)
    comment = models.TextField(null=True, blank=True, verbose_name='Комментарий')

    class Meta:
        ordering = ['-ordered_at']

    def __unicode__(self):
        return self.name
