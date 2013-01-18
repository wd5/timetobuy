$(document).ready(function() {
    var field_cart = $('.field-cart').find('p');
    var cart_id = field_cart.text();
    field_cart.html('<a href="/admin/cart/cartitem/' + cart_id + '"target="_blank">Корзина</a>')
});