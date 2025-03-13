from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee_profile')
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    hire_date = models.DateField()
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.position})"