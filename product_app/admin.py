from django.contrib import admin
from .models import Category, Product, Currency, Price

from modeltranslation.admin import TranslationAdmin

# Модель категории
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}

class PriceInline(admin.TabularInline):
    model = Price
    raw_id_field = ['product']
    max_num = 2


# Модель товара
class ProductAdmin(TranslationAdmin):
    list_display = ['name', 'slug', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['stock', 'available']
    prepopulated_fields = {'slug': ('name', )}
    inlines = [PriceInline]


class PriceAdmin(admin.ModelAdmin):
    list_display = ['product', 'currency', 'value']
    list_filter = ['product', 'currency']
    list_editable = ['value']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Currency)
admin.site.register(Price, PriceAdmin)