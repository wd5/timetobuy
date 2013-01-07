from django.conf.urls import patterns, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('catalog.views',
    url(r'^$', 'main', name='main-page'),
    url(r'^section/(?P<slug>[-\w]+)/$', 'section', name="section-page"),
    url(r'^category/(?P<slug>[-\w]+)/$', 'section', name="category-page"),
    url(r'^brand/(?P<slug>[-\w]+)/$', 'section', name="brand-page"),
)