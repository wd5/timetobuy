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

    @models.permalink
    def get_absolute_url(self):
        return ('brand-page', [str(self.slug)])


class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name=u'Название')
    slug = models.SlugField(max_length=50, unique=True, verbose_name=u'Ссылка')
    category = models.ForeignKey(BrandsCategory, verbose_name=u'Категория бренда')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = u'Бренды'

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
        return ('section-page', [str(self.slug)])

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
        return ('category-page', [str(self.slug)])

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
    price = models.DecimalField(max_digits=9,decimal_places=0, verbose_name=u'Цена')
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
    gender = models.IntegerField(choices=GENGER_CHOICES, blank=True, null=True, verbose_name=u'Пол')
    mechanism = models.IntegerField(choices=MECHANISM_CHOICES, blank=True, null=True, verbose_name=u'Механизм')
    body = models.IntegerField(choices=BODY_CHOICES, blank=True, null=True, verbose_name=u'Корпус')
    bracelet = models.IntegerField(choices=BRACELET_CHOICES, blank=True, null=True, verbose_name=u'Браслет')
    bracelet_length = models.IntegerField(choices=BRACELET_LENGTH_CHOICES, blank=True, null=True, verbose_name=u'Длина браслета')
    window = models.IntegerField(choices=WINDOW_CHOICES, blank=True, null=True, verbose_name=u'Стекло')
    waterproof = models.IntegerField(choices=WATERPROOF_CHOICES, blank=True, null=True, verbose_name=u'Водозащита')
    guarantee = models.IntegerField(choices=GENGER_CHOICES, blank=True, null=True, verbose_name=u'Гарантия')
    color = models.IntegerField(choices=COLOR_CHOICES, blank=True, null=True, verbose_name=u'Цвет ремня/браслета')
    time_indication = models.IntegerField(choices=TIME_INDICATION_CHOICES, blank=True, null=True, verbose_name=u'Индикация времени')
    coated_housing = models.IntegerField(choices=COATED_HOUSING_CHOICES, blank=True, null=True, verbose_name=u'Покрытие корпуса')
    case_form = models.IntegerField(choices=CASE_FORM_CHOICES, blank=True, null=True, verbose_name=u'Форма корпуса')
    coating_bracelet = models.IntegerField(choices=COATING_BRACELET_CHOICES, blank=True, null=True, verbose_name=u'Покрытие браслета')
    dial_color = models.IntegerField(choices=DIAL_COLOR_CHOICES, blank=True, null=True, verbose_name=u'Цвет циферблата')
    calendar = models.IntegerField(choices=CALENDAR_CHOICES, blank=True, null=True, verbose_name=u'Календарь')
    chronograph = models.IntegerField(choices=CHRONOGRAPH_CHOICES, blank=True, null=True, verbose_name=u'Хронограф')
    type_of_lock = models.IntegerField(choices=TYPE_OF_LOCK_CHOICES, blank=True, null=True, verbose_name=u'Тип застежки')
    battery = models.IntegerField(choices=BATTERY_CHOICES, blank=True, null=True, verbose_name=u'Батарея')
    gps = models.IntegerField(choices=GPS_CHOICES, blank=True, null=True, verbose_name=u'GPS')
    digit = models.IntegerField(choices=DIGIT_CHOICES, blank=True, null=True, verbose_name=u'Цифры')
    format = models.IntegerField(choices=FORMAT_TIME_CHOICES, blank=True, null=True, verbose_name=u'Формат')
    seconds = models.IntegerField(choices=SECOND_ARROW_CHOICES, blank=True, null=True, verbose_name=u'Секундная стрелка')
    skeleton = models.IntegerField(choices=SCELETON_CHOICES, blank=True, null=True, verbose_name=u'Скелетон')
    boom = models.IntegerField(choices=BOOM_CHOICES, blank=True, null=True, verbose_name=u'Противоударные')
    auto_battery = models.IntegerField(choices=AUTO_BATTERY_CHOICES, blank=True, null=True, verbose_name=u'Автоподзавод')
    anti_reflective = models.IntegerField(choices=AUTO_BATTERY_CHOICES, blank=True, null=True, verbose_name=u'Антибликовое покрытие стекла')
    stone = models.IntegerField(choices=STONE_CHOICES, blank=True, null=True, verbose_name=u'Камень-вставка')
    clock_accuracy = models.IntegerField(choices=CLOCK_ACCURACY_CHOICES, blank=True, null=True, verbose_name=u'Точность хода')
    alarm = models.IntegerField(choices=ALARM_CHOICES, blank=True, null=True, verbose_name=u'Будильник')
    pulse = models.IntegerField(choices=PULSE_CHOICES, blank=True, null=True, verbose_name=u'Пульсометр')
    flash_light_display = models.IntegerField(choices=FLASH_LIGHT_DISPLAY_CHOICES, blank=True, null=True, verbose_name=u'Подсветка дисплея')
    flash_light_arrow = models.IntegerField(choices=FLASH_LIGHT_ARROW_CHOICES, blank=True, null=True, verbose_name=u'Подсветка стрелок')
    second_time = models.IntegerField(choices=SECOND_TIME_CHOICES, blank=True, null=True, verbose_name=u'Второй часовой пояс')
    note = models.IntegerField(choices=NOTE_CHOICES, blank=True, null=True, verbose_name=u'Записная книжка')
    second_timer = models.IntegerField(choices=SECOND_TIMER_CHOICES, blank=True, null=True, verbose_name=u'Секундомер')
    compass = models.IntegerField(choices=COMPASS_CHOICES, blank=True, null=True, verbose_name=u'Компас')
    timer = models.IntegerField(choices=TIMER_CHOICES, blank=True, null=True, verbose_name=u'Таймер')
    thermometer = models.IntegerField(choices=THERMOMETER_CHOICES, blank=True, null=True, verbose_name=u'Термометр')
    altimeter = models.IntegerField(choices=ALTIMETER_CHOICES, blank=True, null=True, verbose_name=u'Высотомер')
    memory = models.IntegerField(choices=MEMORY_CHOICES, blank=True, null=True, verbose_name=u'Встроенная память')
    weight = models.IntegerField(choices=WEIGHT_CHOICES, blank=True, null=True, verbose_name=u'Вес часов')
    size = models.IntegerField(choices=SIZE_CHOICES, blank=True, null=True, verbose_name=u'Размер часов')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = u'Часы'
