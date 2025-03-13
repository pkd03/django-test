from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'description')
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Thông tin sản phẩm', {
            'fields': ('name', 'description', 'price')
        }),
        ('Kho hàng', {
            'fields': ('stock',)
        }),
        ('Thời gian', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    # Hiển thị giá dạng tiền tệ
    def formatted_price(self, obj):
        return f"${obj.price:.2f}"
    formatted_price.short_description = 'Giá'
    
    # Thêm vào list_display để thay thế price
    list_display = ('name', 'formatted_price', 'stock', 'created_at')