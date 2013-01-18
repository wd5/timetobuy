          # -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.mail import send_mail
import threading
import json
from django.core import urlresolvers
from django.template import RequestContext
from forms import OrderForm
from models import CartProduct, CartItem
import cart
from django.conf import settings

def show_cart(request):
    is_order = False
    form = OrderForm()
    # Содержимое корзины
    cart_items = cart.get_cart_items(request)
    # Высчитывается скидка и общая стоимость
    if cart_items:
        subtotal_class = cart.Subtotal(request)
        cart_subtotal = subtotal_class.subtotal()
        discount = subtotal_class.discount
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            cartitem = CartItem.objects.get(cart_id=cart._cart_id(request))
            new_form.cart = cartitem
            if not new_form.delivery:
                new_form.delivery = 3
            new_form.subtotal = cart_subtotal
            new_form.save()
            t = threading.Thread(target= send_mail, args=[
                u'Заказ от %s' % (form.cleaned_data['name']),
                u'Имя: %s \nТелефон: %s\nEmail: %s'
                % (form.cleaned_data['name'],
                   form.cleaned_data['phone'],
                   form.cleaned_data['email']),
                settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER], 'fail_silently=False'])
            t.setDaemon(True)
            t.start()
            is_order = True
    # Если заказ сделан
    if is_order:
        # Удаляю сессию у клиента
        del request.session['cart_id']
        # Очищаю корзину клиента
        cart_items = False
    return render_to_response("cart.html", locals(), context_instance=RequestContext(request))

def add_to_cart(request):
    cart.add_to_cart(request)
    results = {'url': urlresolvers.reverse('show_cart')}
    response = json.dumps(results)
    return HttpResponse(response, mimetype= "application/json")

def remove_cart_item(request, slug):
    item = CartProduct.objects.get(id=slug)
    cartitem = item.cartitem
    item.delete()
    subtotal = 0
    items = CartProduct.objects.filter(cartitem=cartitem)
    for i in items:
        subtotal += int(i.product.price) * i.quantity
    count_box = cart.cart_count(request)
    results = {'result': True, 'subtotal' : str(subtotal), 'count_box' : str(count_box)}
    response = json.dumps(results)
    return HttpResponse(response, mimetype= "application/json")
