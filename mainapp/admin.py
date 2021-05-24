from django.contrib import admin

from mainapp.models import ProductCategory, Product

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'prise', 'quantity')
    fields = ('name', 'image', 'description', ('prise', 'quantity'), 'category')
    ordering = ('prise',)
    search_fields = ('name',)

