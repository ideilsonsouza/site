from django.contrib import admin
from backend.system.models.product import SysProduct

@admin.register(SysProduct)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = [  'code' ]