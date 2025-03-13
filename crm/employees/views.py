from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filterset_fields = ['department', 'position']
    search_fields = ['user__first_name', 'user__last_name', 'department', 'position']