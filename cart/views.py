          # -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
import json
from django.core import urlresolvers
from django.template import RequestContext
from forms import OrderForm
import cart

def show_cart(request):
    is_order = False
    form = OrderForm()
    # Содержимое корзины
    cart_items = cart.get_cart_items(request)
    if request.method == 'POST':
        postdata = request.POST.copy()
        if 'Remove' in postdata:
            cart.remove_from_cart(request)
        elif 'Update' in postdata:
            cart.update_cart(request)
        else:
            form = OrderForm(request.POST)
            if form.is_valid():
                # Пишу клиента в базу
                cart.save_client(request, form)
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
