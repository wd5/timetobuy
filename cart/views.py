          # -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
import json
from django.core import urlresolvers
from django.template import RequestContext
from forms import OrderForm
from models import CartProduct, CartItem
import cart

def show_cart(request):
    is_order = False
    form = OrderForm()
    # Содержимое корзины
    cart_items = cart.get_cart_items(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            cartitem = CartItem.objects.get(cart_id=cart._cart_id(request))
            new_form.cart = cartitem
            if not new_form.delivery:
                new_form.delivery = 3
            new_form.save()
            is_order = True
    # Высчитывается скидка и общая стоимость
    if cart_items:
        subtotal_class = cart.Subtotal(request)
        cart_subtotal = subtotal_class.subtotal()
        discount = subtotal_class.discount
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
    cart = item.cartitem
    item.delete()
    subtotal = 0
    items = CartProduct.objects.filter(cartitem=cart)
    for i in items:
        subtotal += int(i.product.price) * i.quantity
    results = {'result': True, 'subtotal' : str(subtotal)}
    response = json.dumps(results)
    return HttpResponse(response, mimetype= "application/json")
