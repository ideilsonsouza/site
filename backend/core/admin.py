from django.contrib import admin
from django.contrib.auth import get_permission_codename
from django.contrib import messages
from django.utils.translation import ngettext
from backend.core.models import SystemCode



class CoreInline(admin.StackedInline):    
    extra=0
    class Meta:
        abstract = True

class CoreAdmin(admin.ModelAdmin):
    actions = ['set_inactive','set_active']
    date_hierarchy='created_at'
    

    @admin.action(permissions=["change"], description="Inativar registro")
    def set_inactive(self, request, queryset):
        updated = queryset.update(active=False)
        self.message_user(
            request,
            ngettext(
                "%d registro foi inativado com sucesso.",
                "%d registros foram inativados com sucesso.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )

    @admin.action(permissions=["change"], description="Ativar registro")
    def set_active(self, request, queryset):
        updated = queryset.update(active=True)
        self.message_user(
            request,
            ngettext(
                "%d registro foi ativado com sucesso.",
                "%d registros foram ativados com sucesso.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )
    
    class Meta:
        abstract = True

@admin.register(SystemCode)
class AdminSystemCode(CoreAdmin):
    pass
