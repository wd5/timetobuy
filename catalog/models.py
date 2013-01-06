    # -*- coding: utf-8 -*-
from django.db import models
from catalog.fields import ThumbnailImageField
from catalog.clock_features import GENGER_CHOICES

class BrandsCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    logo = models.ImageField(upload_to='static/img/brand_image')

class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

class Collection(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    brand = models.ForeignKey(Brand)

class Section(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    sort_number = models.IntegerField()

    class Meta:
        ordering = ['sort_number']
        verbose_name_plural = u'Секции товара'

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('catalog.views.section', [str(self.slug)])

class Category(models.Model):
    name = models.CharField(max_length=50)
    section = models.ForeignKey(Section)
    slug = models.SlugField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    position = models.PositiveSmallIntegerField("Position")

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['position']
        verbose_name_plural = u'Категории часов'

    @models.permalink
    def get_absolute_url(self):
        return ('catalog-page', [str(self.slug)])

class CategoryProduct(models.Model):
    category = models.ForeignKey('Category')
    product = models.ForeignKey('Product', verbose_name=u'Товар')
    position = models.PositiveSmallIntegerField("Position")

    class Meta:
        ordering = ['position']

class Product(models.Model):
    category = models.ManyToManyField(Category, verbose_name=u'Категория', through=CategoryProduct)
    brand = models.ForeignKey(Brand)
    name = models.CharField(max_length=255, unique=True, verbose_name=u'Название')
    slug = models.SlugField(max_length=255, unique=True, verbose_name=u'Ссылка')
    price = models.DecimalField(max_digits=9,decimal_places=2, verbose_name=u'Цена')
    thumbnail_image = ThumbnailImageField(upload_to='static/img/products_image', thumb_width=200, thumb_height=200, completion="thumb" )
    # Метаданные товара
    is_active = models.BooleanField(default=True, verbose_name='Активный')
    # Временные отметки
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('product-page', [str(self.slug)])

    class Meta:
        verbose_name_plural = u'Товар'

class ProductPhoto(models.Model):
    item = models.ForeignKey(Product)
    image = ThumbnailImageField(upload_to='products_image', thumb_width=460, thumb_height=350, completion="resized" )

    class Meta:
        ordering = ['item']
        verbose_name_plural = 'Фото часов'

    def __unicode__(self):
        return self.image.name

    @models.permalink
    def get_absolute_url(self):
        return ('item_detail', None, {'object_id': self.id})

class Clock(Product):
    gender = models.IntegerField(choices=GENGER_CHOICES)
