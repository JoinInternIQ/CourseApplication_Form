from django.contrib import admin
from django.utils.html import format_html
from import_export.admin import ExportMixin
from import_export import resources
from .models import InternshipApplication

# Resource class for export
class InternshipApplicationResource(resources.ModelResource):
    class Meta:
        model = InternshipApplication
        # list of fields to export (you can adjust)
        exclude = ('photo')  # don't export image blobs

@admin.register(InternshipApplication)
class InternshipApplicationAdmin(ExportMixin, admin.ModelAdmin):  # Add ExportMixin
    resource_class = InternshipApplicationResource

    list_display = (
        'name', 'gender', 'dob', 'phone', 'email', 'address',
        'department', 'year_of_study', 'batch_from', 'batch_to',
        'college_name', 'domains'
    )


    search_fields = [
        'name', 'email', 'phone', 'college_name'
    ]
    
    list_filter = [
        'gender', 'domains',
        'year_of_study', 'department', 'college_name'
    ]

    ordering = ['name']

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="100"/>', obj.photo.url)
        return "-"
    photo_preview.short_description = "Photo"

