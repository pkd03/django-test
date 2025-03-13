from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'department', 'position', 'phone', 'hire_date')
    list_filter = ('department', 'position', 'hire_date')
    search_fields = ('user__first_name', 'user__last_name', 'user__email', 'department', 'position')
    ordering = ('user__last_name',)
    
    fieldsets = (
        ('Thông tin người dùng', {
            'fields': ('user',)
        }),
        ('Thông tin công việc', {
            'fields': ('department', 'position', 'phone', 'hire_date')
        }),
    )
    
    def full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    full_name.short_description = 'Họ và tên'
    
    # Liên kết đến user admin
    def view_user(self, obj):
        from django.urls import reverse
        from django.utils.html import format_html
        url = reverse("admin:auth_user_change", args=[obj.user.id])
        return format_html('<a href="{}">Xem chi tiết</a>', url)
    view_user.short_description = 'Tài khoản'
    
    # Thêm vào list_display
    list_display = ('full_name', 'department', 'position', 'phone', 'hire_date', 'view_user')