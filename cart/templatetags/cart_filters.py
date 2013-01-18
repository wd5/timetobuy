from django import template
from cart import cart

register = template.Library()

@register.inclusion_tag("tags/cart_box.html")
def cart_box(request):
    box_count = cart.cart_count(request)
    subtotal_class = cart.Subtotal(request)
    return {
        'box_count': box_count,
        'subtotal': subtotal_class.subtotal(),
    }

@register.filter
def multiply(value, arg):
    return int(value) * int(arg)
