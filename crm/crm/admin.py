from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.db.models import Count
from customers.models import Customer
from products.models import Product
from tasks.models import Task
from datetime import datetime, timedelta

class DashboardAdmin(admin.AdminSite):
    site_header = "CRM Admin"
    site_title = "CRM Admin Portal"
    index_title = "Quản lý CRM"
    
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('dashboard/', self.admin_view(self.dashboard_view), name='dashboard'),
        ]
        return custom_urls + urls
    
    def dashboard_view(self, request):
        # Thống kê theo ngày
        thirty_days_ago = datetime.now() - timedelta(days=30)
        
        customers_count = Customer.objects.count()
        new_customers = Customer.objects.filter(created_at__gte=thirty_days_ago).count()
        
        products_count = Product.objects.count()
        
        tasks_by_status = Task.objects.values('status').annotate(count=Count('id'))
        tasks_by_status_dict = {item['status']: item['count'] for item in tasks_by_status}
        
        context = {
            'customers_count': customers_count,
            'new_customers': new_customers,
            'products_count': products_count,
            'tasks_by_status': tasks_by_status_dict,
            'title': 'Dashboard',
        }
        return render(request, 'admin/dashboard.html', context)