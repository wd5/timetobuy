from django.contrib import admin
from catalog.models import *
from cart.models import *
from sorl.thumbnail.admin import AdminImageMixin
from markitup.widgets import AdminMarkItUpWidget

class PhotoInline(AdminImageMixin, admin.StackedInline):
    model = ProductPhoto

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
    inlines = [CategoryProductinline, PhotoInline]
    list_per_page = 50
    ordering = ['name']
    search_fields = ['name', 'description']
    prepopulated_fields = {'name':('article',),'slug' : ('name',)}

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

class ClientsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'ordered_at',)
    list_display_links = ('name',)
    exclude = ('referrer',)
    readonly_fields=('cart',)

    class Media:
        from django.conf import settings
        static_url = getattr(settings, 'STATIC_URL', '/static/')
        js = [ static_url+'/js/jquery-1.8.2.min.js', static_url+'/js/cart-link.js', ]

admin.site.register(Client, ClientsAdmin)

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment', 'ordered_at', 'is_moderate')

admin.site.register(Comment, CommentsAdmin)

class CartProductinline(admin.TabularInline):
    model = CartProduct

class CartItemAdmin(admin.ModelAdmin):
    inlines = [CartProductinline]
    exclude = ('cart_id',)
    model = ProductPhoto

admin.site.register(CartItem, CartItemAdmin)
