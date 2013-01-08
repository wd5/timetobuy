from django.contrib import admin
from catalog.models import *
from markitup.widgets import AdminMarkItUpWidget

class CategoryProductinline(admin.TabularInline):
    model = CategoryProduct
    sortable_field_name = "position"

class CategoryInline(admin.TabularInline):
    fields = ('name', 'position',)
    model = Category
    sortable_field_name = "position"

class SectionsAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Section, SectionsAdmin)

class ClocksAdmin(admin.ModelAdmin):
    inlines = [CategoryProductinline]
    list_per_page = 50
    ordering = ['name']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug' : ('name',)}

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'description':
            kwargs['widget'] = AdminMarkItUpWidget()
        return super(ClocksAdmin, self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(Clock, ClocksAdmin)

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description',]
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Category, CategoriesAdmin)

class BrandsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Brand, BrandsAdmin)

class BrandsCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(BrandsCategory, BrandsCategoryAdmin)
