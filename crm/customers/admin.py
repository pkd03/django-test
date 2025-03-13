from django.contrib import admin
from rangefilter.filters import DateRangeFilter
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Customer

class CustomerResource(resources.ModelResource):
    class Meta:
        model = Customer
        skip_unchanged = True
        report_skipped = True
        fields = ('id', 'name', 'email', 'phone', 'company', 'address', 'created_at', 'updated_at')

@admin.register(Customer)
class CustomerAdmin(ImportExportModelAdmin):
    resource_class = CustomerResource
    
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'company', 'created_at', 'updated_at')
    list_filter = ('created_at', 'company')
    search_fields = ('name', 'email', 'company', 'address')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Thông tin cơ bản', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Thông tin công ty', {
            'fields': ('company', 'address')
        }),
        ('Thông tin thời gian', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    list_filter = (
        ('created_at', DateRangeFilter),
        'company',
    )
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs