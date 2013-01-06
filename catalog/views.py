# -*- coding: utf-8 -*-
from catalog.models import Section, Product, BrandsCategory
import re
from django.db.models.query_utils import Q
from django.shortcuts import get_object_or_404, render_to_response, render
from django.core import urlresolvers
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
import threading
from django.core.mail import send_mail

def main(request):
    return render(request, 'main.html', locals())

def section(request, section_slug):
    section = Section.objects.get(slug=section_slug)
    products = Product.objects.filter(category__section=section)
    brands_cat = BrandsCategory.objects.all()
    products_cat = []
    products_brand = []
    for product in products:
        products_cat.append(product.brand.category.id)
        products_brand.append(product.brand.id)
    return render(request, 'catalog.html', locals())
