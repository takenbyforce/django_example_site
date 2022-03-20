from django.contrib import admin

from .models import ProjectEntry


class ProjectAdmin(admin.ModelAdmin):
    autocomplete_fields = ('owner',)
    list_display = ('name', 'rating', 'owner')
    list_filter = ('rating', 'owner')

    def get_changeform_initial_data(self, request):
        """Use current user as a default for `owner` field"""
        initial = super().get_changeform_initial_data(request)
        return {**initial, 'owner': request.user}


admin.site.register(ProjectEntry, ProjectAdmin)
