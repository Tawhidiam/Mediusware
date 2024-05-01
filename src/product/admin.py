from django.contrib import admin
from .models import Variant, Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'sku':('title',) }


admin.site.register(Variant, )
admin.site.register(Product, ProductAdmin)
