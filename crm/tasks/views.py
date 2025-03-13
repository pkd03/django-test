# tasks/views.py
from rest_framework import viewsets
from django_filters import rest_framework as filters
from .models import TaskBoard, Task
from .serializers import TaskBoardSerializer, TaskSerializer

class TaskFilter(filters.FilterSet):
    status = filters.CharFilter(field_name='status')
    assignee = filters.NumberFilter(field_name='assignee__id')
    
    class Meta:
        model = Task
        fields = ['status', 'assignee']

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filterset_class = TaskFilter
    search_fields = ['title', 'description']

class TaskBoardViewSet(viewsets.ModelViewSet):
    queryset = TaskBoard.objects.all()
    serializer_class = TaskBoardSerializer
    search_fields = ['name', 'description']