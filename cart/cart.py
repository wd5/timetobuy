          # -*- coding: utf-8 -*-
from models import CartItem, Client, CartProduct
from catalog.models import *
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
import threading
import decimal
import random

CART_ID_SESSION_KEY = 'cart_id'

# Пишет сесссию если ее не существует и возвращает существующую или созданную
def _cart_id(request):
    if request.session.get(CART_ID_SESSION_KEY,'') == '':
        request.session[CART_ID_SESSION_KEY] = _generate_cart_id()
    return request.session[CART_ID_SESSION_KEY]

# Генерирует cart ID для сессии
def _generate_cart_id():
    cart_id = ''
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
    cart_id_length = 50
    for y in range(cart_id_length):
        cart_id += characters[random.randint(0, len(characters)-1)]
    return cart_id

# Возвращает все объекты корзины
def get_cart_items(request):
    try:
        cartid = CartItem.objects.get(cart_id = _cart_id(request))
        return CartProduct.objects.filter(cartitem=cartid)
    except :
        return False

# Возвращает колиство объектов(наименований товара) в корзине
def cart_count(request):
    if CartItem.objects.filter(cart_id = _cart_id(request)):
        quantity = 0
        for i in CartProduct.objects.filter(cartitem__cart_id =_cart_id(request)):
            quantity += i.quantity
        return quantity
    else:
        return 0

# Добавляет товар в корзину
def add_to_cart(request):
    postdata = request.POST.copy()
    # Получаю название заказанного продукта
    product_slug = postdata.get('product_slug','')
    quantity = 1
    product_in_cart = False
    # Получаю заказанный продукт
    p = get_object_or_404(Product, slug=product_slug)
    # Если корзина уже есть в базe
    if CartItem.objects.filter(cart_id = _cart_id(request)):
        # Получаю все продукты в корзине
        cart = CartItem.objects.get(cart_id = _cart_id(request))
        cart_products = CartProduct.objects.filter(cartitem=cart.id)
        # Если корзина пуста то добавляю товар
        if not cart_products:
            cart = CartItem.objects.get(cart_id = _cart_id(request))
            CartProduct(cartitem = cart, product = p).save()
        else:
            cart_items = []
            # Проверяю есть ли такой продукт уже в корзине
            for item in cart_products:
                # Если уже есть то обновляю количество
                if item.product_id == p.id:
                    item.quantity += quantity
                    item.save()
                    cart_items.append(item.product_id)
            # Если товара нету в коржине то добавляю
            if p.id not in cart_items:
                cart = CartItem.objects.get(cart_id = _cart_id(request))
                CartProduct(cartitem = cart, product = p).save()
    # Если нету то добавляю
    else:
        ci = CartItem()
        ci.cart_id = _cart_id(request)
        ci.save()
        # И добавляю его заказ в корзину
        cart = CartItem.objects.get(cart_id = _cart_id(request))
        CartProduct(cartitem = cart, product = p).save()


# Обновляет количество товара в корзине
def update_cart(request):
    postdata = request.POST.copy()
    item_id = postdata['item_id']
    quantity = postdata['quantity']
    cart_item = get_object_or_404(CartProduct, id=item_id)
    if cart_item:
        if int(quantity) > 0:
            cart_item.quantity = int(quantity)
            cart_item.save()
        else:
            remove_from_cart(request)

# Удаляет товар из корзины
def remove_from_cart(request):
    postdata = request.POST.copy()
    item_id = postdata['item_id']
    cart_item = get_object_or_404(CartProduct, id=item_id)
    if cart_item:
        cart_item.delete()

# Сохраняет клиента в базу
def save_client(request, form):
    cart = CartItem.objects.get(cart_id=_cart_id(request))
    subtotal_class = Subtotal(request)

    ci = Client()
    ci.cart = cart
    ci.name = form.cleaned_data['name']
    ci.surname = form.cleaned_data['surname']
    ci.patronymic = form.cleaned_data['patronymic']
    ci.city = form.cleaned_data['city']
    ci.postcode = form.cleaned_data['postcode']
    ci.phone = form.cleaned_data['phone']
    ci.address = form.cleaned_data['address']
    ci.email = form.cleaned_data['email']
    ci.subtotal = subtotal_class.subtotal()
    ci.discount = subtotal_class.discount
    ci.referrer = request.COOKIES.get('REFERRER', None)
    ci.save()
    # Обновляю количество товара на складе
    products = CartProduct.objects.filter(cartitem=cart)
    for product in products:
        store_product = Product.objects.get(name=product.product)
        store_product.quantity -= product.quantity
        store_product.save()

# Высчитывает общую стоимость товаров в корзине + скидку
class Subtotal:
    def __init__(self, request):
        self.request = request
        self.discount = 0

    def subtotal(self):
        cart_total = 0
        cart_discount_total = 0
        # Получаю все товары в корзине
        cart_products = get_cart_items(self.request)
        discount_quantity = 0
        if cart_products:
            for cart_item in cart_products:
                cart_total += cart_item.product.price * cart_item.quantity
        cart_total -= self.discount
        return cart_total

# Высылает email о покупке и покупатале
def send_admin_email(request, cart_items, form, cart_subtotal, discount):
    products_for_email = ""
    for item in cart_items:
        products_for_email += u"%s:%s шт  http://my-spy.ru%s\n" % (item.product.name,
                                          item.quantity, item.product.get_absolute_url())
    t = threading.Thread(target= send_mail, args=[
        u'Заказ от %s %s' % (form.cleaned_data['name'], form.cleaned_data['surname'] ),
        u'Имя: %s %s %s \nГород: %s\nИндекс: %s\nТелефон: %s\nАдрес: %s\nEmail: %s\n\n%s\nВсего на сумму: %s руб\nСкидка: %s руб\n\nПришел с: %s'
        % (form.cleaned_data['surname'], form.cleaned_data['name'], form.cleaned_data['patronymic'],
        form.cleaned_data['city'], form.cleaned_data['postcode'], form.cleaned_data['phone'],
        form.cleaned_data['address'], form.cleaned_data['email'], products_for_email, cart_subtotal, discount, request.COOKIES.get('REFERRER', None) ),
        EMAIL_HOST_USER, [EMAIL_HOST_USER], 'fail_silently=False'])
    t.setDaemon(True)
    t.start()

# Высылает email клиенту о покупке
def send_client_email(cart_items, form, cart_subtotal):
    products_for_email = ""
    for item in cart_items:
        products_for_email += u"%s:%s шт  http://my-spy.ru%s\n" % (item.product.name,
                                          item.quantity, item.product.get_absolute_url())
    t = threading.Thread(target= send_mail, args=[
        u'Ваш заказ от my-spy',
        u'Здравствуйте %s,\n\nВы оформили у нас заказ на:\n%s\nВсего на сумму: %s руб\n\nВ ближайшее время наш менеджер с вами свяжется.\nС Уважением, my-spy.ru' %
        (form.cleaned_data['name'], products_for_email, cart_subtotal ),
        EMAIL_HOST_USER, [form.cleaned_data['email']], 'fail_silently=False'])
    t.setDaemon(True)
    t.start()
