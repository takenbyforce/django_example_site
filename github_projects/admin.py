from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin

from .models import ProjectEntry, WebhookConfig


class AutoUserModelAdmin(admin.ModelAdmin):
    autocomplete_fields = ('owner',)

    def get_changeform_initial_data(self, request):
        """Use current user as a default for `owner` field"""
        initial = super().get_changeform_initial_data(request)
        return {**initial, 'owner': request.user}


class ProjectAdmin(AutoUserModelAdmin):
    list_display = ('name', 'rating', 'owner')
    list_filter = ('rating', 'owner')


class WebhookAdmin(AutoUserModelAdmin):
    list_display = ('url', 'owner')
    list_filter = ('owner',)


admin.site.register(ProjectEntry, ProjectAdmin)
admin.site.register(WebhookConfig, WebhookAdmin)

TokenAdmin.autocomplete_fields = ('user',)
