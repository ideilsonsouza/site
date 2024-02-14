from django.contrib import admin
from backend.system.models.client import SysClient


@admin.register(SysClient)
class ClientAdmin(admin.ModelAdmin):
    readonly_fields = [  'code' ]