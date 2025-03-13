from django.db import models
from employees.models import Employee

class TaskStatus(models.TextChoices):
    TODO = 'TODO', 'To Do'
    IN_PROGRESS = 'IN_PROGRESS', 'In Progress'
    REVIEW = 'REVIEW', 'In Review'
    DONE = 'DONE', 'Done'

class TaskBoard(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    board = models.ForeignKey(TaskBoard, on_delete=models.CASCADE, related_name='tasks')
    status = models.CharField(
        max_length=20,
        choices=TaskStatus.choices,
        default=TaskStatus.TODO
    )
    assignee = models.ForeignKey(
        Employee, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='assigned_tasks'
    )
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title