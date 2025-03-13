from rest_framework import serializers
from .models import TaskBoard, Task
from employees.serializers import EmployeeSerializer

class TaskSerializer(serializers.ModelSerializer):
    assignee_details = EmployeeSerializer(source='assignee', read_only=True)
    
    class Meta:
        model = Task
        fields = '__all__'

class TaskBoardSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    
    class Meta:
        model = TaskBoard
        fields = '__all__'