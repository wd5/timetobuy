          # -*- coding: utf-8 -*-
from django.db import models
from catalog.models import Product

class CartProduct(models.Model):
    cartitem = models.ForeignKey('CartItem')
    product = models.ForeignKey(Product, verbose_name=u'Товар')
    quantity = models.IntegerField(default=1, verbose_name=u'Количество')

class CartItem(models.Model):
    cart_id = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    product = models.ManyToManyField(Product, through=CartProduct)

    class Meta:
        db_table = 'cart_item'

# Механизм
DELIVERY_CHOICES = (
  (0, u'Москва'),
  (1, u'Подмосковье'),
  (2, u'Россия'),
  (2, u'Не указано'),
)

class Client(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'Имя')
    phone = models.CharField(max_length=20, verbose_name=u'Телефон')
    email = models.EmailField()
    address = models.CharField(max_length=500, null=True, blank=True, verbose_name=u'Адрес')
    comment = models.TextField(null=True, blank=True, verbose_name=u'Комментарий')
    delivery = models.IntegerField(choices=DELIVERY_CHOICES, blank=True, null=True, verbose_name=u'Доставка')
    referrer = models.URLField(null=True, blank=True, verify_exists=False, max_length=500)
    cart = models.ForeignKey(CartItem)
    subtotal = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2, verbose_name=u'Сумма')
    ordered_at = models.DateTimeField(auto_now_add=True )

    class Meta:
        ordering = ['-ordered_at']

    def __unicode__(self):
        return self.name
