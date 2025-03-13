"""
URL configuration for crm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

# Import viewsets
from customers.views import CustomerViewSet
from products.views import ProductViewSet
from employees.views import EmployeeViewSet
from tasks.views import TaskBoardViewSet, TaskViewSet

# Create router and register viewsets
router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'products', ProductViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'taskboards', TaskBoardViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    
    # Swagger UI endpoints
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
    # JWT authentication
    path('api/auth/', include('authentication.urls')),
]

ADMIN_SITE_HEADER = "CRM Admin"
ADMIN_SITE_TITLE = "CRM Admin Portal"
ADMIN_INDEX_TITLE = "Quản lý CRM"


admin.site.site_header = "CRM Admin"
admin.site.site_title = "CRM Admin Portal"
admin.site.index_title = "Quản lý CRM"