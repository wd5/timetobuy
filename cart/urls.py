from django.conf.urls import patterns, url

urlpatterns = patterns('cart.views',
    url(r'^$', 'show_cart', name="show_cart"),
    url(r'^add/$', 'add_to_cart', name="add-to-cart"),
    url(r'^rm-item/(?P<slug>[-\w]+)/$', 'remove_cart_item', name="remove-cart-item"),
)

