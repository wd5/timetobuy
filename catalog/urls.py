from django.conf.urls import patterns, url

urlpatterns = patterns('catalog.views',
    url(r'^$', 'main', name='main-page'),
    url(r'^section/$', 'section', name="section-page"),
    url(r'^section/(?P<slug>[-\w]+)/$', 'section', name="section-page"),
    url(r'^category/(?P<slug>[-\w]+)/$', 'section', name="category-page"),
    url(r'^brand/(?P<slug>[-\w]+)/$', 'section', name="brand-page"),
    url(r'^clock/(?P<slug>[-\w]+)/$', 'clock', name="clock-page"),
    url(r'^post-comment/$', 'post_comment', name="post-comment"),
)