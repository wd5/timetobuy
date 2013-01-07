# -*- coding: utf-8 -*-
from catalog.models import Section, Product, Clock, BrandsCategory
from django.shortcuts import get_object_or_404, render_to_response, render

def main(request):
    return render(request, 'main.html', locals())

def section(request, section_slug):
    params = request.GET.dict()

    section = Section.objects.get(slug=section_slug)
    chosen_params = []
    price_range = False
    if params.has_key('price-range'):
        price_range = params['price-range']
        params.pop('price-range')
    if params.has_key('brandscat'):
        brands_cat_filter = params['brandscat']
        chosen_params.append(['brandscat', u'Бренд', BrandsCategory.objects.get(id=brands_cat_filter).name])
        params.pop('brandscat')
        clocks = Clock.objects.filter(category__section=section).filter(**params).filter(brand__category_id=brands_cat_filter)
    else:
        clocks = Clock.objects.filter(category__section=section).filter(**params)
    for param in params:
        new_p = [param,]
        filter_name = clocks[0]._meta.get_field_by_name(param)[0].verbose_name
        new_p.append(filter_name)
        value = clocks[0].__getattribute__(param)
        if param == 'brand':
            new_p.append(value)
            brand_is_filter = True
        else:
            for item in clocks[0]._meta.get_field_by_name(param)[0].choices:
                if item[0] == value:
                    new_p.append(item[1])
        chosen_params.append(new_p)
    if price_range:
        clocks = clocks.filter(price__range=(int(price_range.split(':')[0]), int(price_range.split(':')[1])))
        chosen_params.append(['price-range', u'Фильтр цены', price_range])
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
    battery = set()
    gps = set()
    digit = set()
    format = set()
    seconds = set()
    skeleton = set()
    boom = set()
    auto_battery = set()
    anti_reflective = set()
    stone = set()
    clock_accuracy = set()
    alarm = set()
    pulse = set()
    flash_light_display = set()
    flash_light_arrow = set()
    second_time = set()
    note = set()
    second_timer = set()
    compass = set()
    timer = set()
    thermometer = set()
    altimeter = set()
    memory = set()
    weight = set()
    size = set()
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
        battery.add((clock.get_battery_display(), clock.battery))
        gps.add((clock.get_gps_display(), clock.gps))
        digit.add((clock.get_digit_display(), clock.digit))
        format.add((clock.get_format_display(), clock.format))
        seconds.add((clock.get_seconds_display(), clock.seconds))
        skeleton.add((clock.get_skeleton_display(), clock.skeleton))
        boom.add((clock.get_boom_display(), clock.boom))
        auto_battery.add((clock.get_auto_battery_display(), clock.auto_battery))
        anti_reflective.add((clock.get_anti_reflective_display(), clock.anti_reflective))
        stone.add((clock.get_stone_display(), clock.stone))
        clock_accuracy.add((clock.get_clock_accuracy_display(), clock.clock_accuracy))
        alarm.add((clock.get_alarm_display(), clock.alarm))
        pulse.add((clock.get_pulse_display(), clock.pulse))
        flash_light_display.add((clock.get_flash_light_display_display(), clock.flash_light_display))
        flash_light_arrow.add((clock.get_flash_light_arrow_display(), clock.flash_light_arrow))
        second_time.add((clock.get_second_time_display(), clock.second_time))
        note.add((clock.get_note_display(), clock.note))
        second_timer.add((clock.get_second_timer_display(), clock.second_timer))
        compass.add((clock.get_compass_display(), clock.compass))
        timer.add((clock.get_timer_display(), clock.timer))
        thermometer.add((clock.get_thermometer_display(), clock.thermometer))
        altimeter.add((clock.get_altimeter_display(), clock.altimeter))
        memory.add((clock.get_memory_display(), clock.memory))
        weight.add((clock.get_weight_display(), clock.weight))
        size.add((clock.get_size_display(), clock.size))
        brands_cat.add(clock.brand.category)
        brands.append(clock.brand.id)
    return render(request, 'catalog.html', locals())
