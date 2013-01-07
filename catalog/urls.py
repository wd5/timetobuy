from django.conf.urls import patterns, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('catalog.views',
    url(r'^$', 'main', name='main-page'),
    url(r'^section/(?P<section_category_slug>[-\w]+)/$', 'section_category', name="section-category-page"),
)