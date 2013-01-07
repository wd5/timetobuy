# -*- coding: utf-8 -*-
from catalog.models import Section, Product, Clock, BrandsCategory
from django.shortcuts import get_object_or_404, render_to_response, render

def main(request):
    return render(request, 'main.html', locals())

def section(request, section_slug):
    params = request.GET.dict()
    section = Section.objects.get(slug=section_slug)
    clocks = Clock.objects.filter(category__section=section).filter(**params)
    genders = set()
    mechanisms = set()
    bodys = set()
    bracelets = set()
    bracelet_lengths = set()
    windows = set()
    waterproofs = set()
    colors = set()
    time_indications = set()
    coated_housings = set()
    case_forms = set()
    coating_bracelets = set()
    dial_colors = set()
    calendars = set()
    chronographs = set()
    type_of_locks = set()
    brands_cat = set()
    brands = []
    for clock in clocks:
        genders.add((clock.get_gender_display(), clock.gender))
        mechanisms.add((clock.get_mechanism_display(), clock.mechanism))
        bodys.add((clock.get_body_display(), clock.body))
        bracelets.add((clock.get_bracelet_display(), clock.bracelet))
        bracelet_lengths.add((clock.get_bracelet_length_display(), clock.bracelet_length))
        windows.add((clock.get_window_display(), clock.window))
        waterproofs.add((clock.get_waterproof_display(), clock.waterproof))
        colors.add((clock.get_color_display(), clock.color))
        time_indications.add((clock.get_time_indication_display(), clock.time_indication))
        coated_housings.add((clock.get_coated_housing_display(), clock.coated_housing))
        case_forms.add((clock.get_case_form_display(), clock.case_form))
        coating_bracelets.add((clock.get_coating_bracelet_display(), clock.coating_bracelet))
        dial_colors.add((clock.get_color_display(), clock.dial_color))
        calendars.add((clock.get_calendar_display(), clock.calendar))
        chronographs.add((clock.get_chronograph_display(), clock.chronograph))
        type_of_locks.add((clock.get_type_of_lock_display(), clock.type_of_lock))
        brands_cat.add(clock.brand.category)
        brands.append(clock.brand.id)
    return render(request, 'catalog.html', locals())
