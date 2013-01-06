    # -*- coding: utf-8 -*-
from django.db import models
from catalog.fields import ThumbnailImageField
from catalog.clock_features import *

class BrandsCategory(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name=u'Название')
    slug = models.SlugField(max_length=50, unique=True, verbose_name=u'Ссылка')
    logo = models.ImageField(upload_to='static/img/brand_image', verbose_name=u'Лого')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = u'Категории брендов'

class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name=u'Название')
    slug = models.SlugField(max_length=50, unique=True, verbose_name=u'Ссылка')
    category = models.ForeignKey(BrandsCategory, verbose_name=u'Категория бренда')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = u'Бренды'

class Collection(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    brand = models.ForeignKey(Brand)

    class Meta:
        verbose_name_plural = u'Коллекции'

class Section(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name=u'Название')
    slug = models.SlugField(max_length=50, unique=True, verbose_name=u'Ссылка')
    is_active = models.BooleanField(default=True, verbose_name=u'Включена')
    sort_number = models.IntegerField(verbose_name=u'Позиция')

    class Meta:
        ordering = ['sort_number']
        verbose_name_plural = u'Секции товара'

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('catalog.views.section', [str(self.slug)])

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'Название')
    section = models.ForeignKey(Section, verbose_name=u'Секция')
    slug = models.SlugField(max_length=50, unique=True, verbose_name=u'Ссылка')
    is_active = models.BooleanField(default=True, verbose_name=u'Включена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u'Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name=u'Дата обдновления')
    position = models.PositiveSmallIntegerField(verbose_name=u'Позиция')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['position']
        verbose_name_plural = u'Категории товара'

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
    brand = models.ForeignKey(Brand, verbose_name=u'Бренд')
    name = models.CharField(max_length=255, unique=True, verbose_name=u'Название')
    slug = models.SlugField(max_length=255, unique=True, verbose_name=u'Ссылка')
    price = models.DecimalField(max_digits=9,decimal_places=2, verbose_name=u'Цена')
    thumbnail_image = ThumbnailImageField(upload_to='static/img/products_image', thumb_width=200, thumb_height=200, completion="thumb", verbose_name=u'Фото')
    # Метаданные товара
    is_active = models.BooleanField(default=True, verbose_name=u'Включен')
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
    gender = models.IntegerField(choices=GENGER_CHOICES, blank=True, null=True)
    mechanism = models.IntegerField(choices=MECHANISM_CHOICES, blank=True, null=True)
    body = models.IntegerField(choices=BODY_CHOICES, blank=True, null=True)
    bracelet = models.IntegerField(choices=BRACELET_CHOICES, blank=True, null=True)
    bracelet_length = models.IntegerField(choices=BRACELET_LENGTH_CHOICES, blank=True, null=True)
    window = models.IntegerField(choices=WINDOW_CHOICES, blank=True, null=True)
    waterproof = models.IntegerField(choices=WATERPROOF_CHOICES, blank=True, null=True)
    guarantee = models.IntegerField(choices=GENGER_CHOICES, blank=True, null=True)
    color = models.IntegerField(choices=COLOR_CHOICES, blank=True, null=True)
    time_indication = models.IntegerField(choices=TIME_INDICATION_CHOICES, blank=True, null=True)
    coated_housing = models.IntegerField(choices=COATED_HOUSING_CHOICES, blank=True, null=True)
    case_form = models.IntegerField(choices=CASE_FORM_CHOICES, blank=True, null=True)
    coating_bracelet = models.IntegerField(choices=COATING_BRACELET_CHOICES, blank=True, null=True)
    dial_color = models.IntegerField(choices=DIAL_COLOR_CHOICES, blank=True, null=True)
    calendar = models.IntegerField(choices=CALENDAR_CHOICES, blank=True, null=True)
    chronograph = models.IntegerField(choices=CHRONOGRAPH_CHOICES, blank=True, null=True)
    type_of_lock = models.IntegerField(choices=TYPE_OF_LOCK_CHOICES, blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = u'Часы'
