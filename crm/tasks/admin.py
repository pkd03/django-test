# tasks/admin.py
from django.contrib import admin
from rangefilter.filters import DateRangeFilter
from .models import TaskBoard, Task

class TaskInline(admin.TabularInline):
    model = Task
    extra = 1
    readonly_fields = ('created_at', 'updated_at')

@admin.register(TaskBoard)
class TaskBoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'task_count', 'created_at')
    search_fields = ('name', 'description')
    inlines = [TaskInline]
    
    def task_count(self, obj):
        return obj.tasks.count()
    task_count.short_description = 'Số công việc'

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'board', 'status', 'assignee', 'due_date', 'created_at')
    list_filter = ('status', 'board', 'due_date')
    search_fields = ('title', 'description', 'assignee__user__first_name', 'assignee__user__last_name')
    ordering = ('-due_date',)
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Thông tin công việc', {
            'fields': ('title', 'description', 'board')
        }),
        ('Trạng thái', {
            'fields': ('status', 'assignee', 'due_date')
        }),
        ('Thông tin thời gian', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    list_filter = (
        'status', 
        'board', 
        ('due_date', DateRangeFilter),
        ('created_at', DateRangeFilter),
    )

    def status_display(self, obj):
        status_colors = {
            'TODO': 'gray',
            'IN_PROGRESS': 'blue',
            'REVIEW': 'orange',
            'DONE': 'green',
        }
        color = status_colors.get(obj.status, 'black')
        return format_html('<span style="color: {}; font-weight: bold;">{}</span>',
                           color, obj.get_status_display())
    status_display.short_description = 'Trạng thái'
    
    list_display = ('title', 'board', 'status_display', 'assignee', 'due_date', 'created_at')
    
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('board', 'assignee', 'assignee__user')
    
    actions = ['mark_as_done', 'mark_as_in_progress']
    
    def mark_as_done(self, request, queryset):
        updated = queryset.update(status='DONE')
        self.message_user(request, f'{updated} công việc đã được đánh dấu hoàn thành.')
    mark_as_done.short_description = "Đánh dấu công việc đã hoàn thành"
    
    def mark_as_in_progress(self, request, queryset):
        updated = queryset.update(status='IN_PROGRESS')
        self.message_user(request, f'{updated} công việc đã được đánh dấu đang thực hiện.')
    mark_as_in_progress.short_description = "Đánh dấu công việc đang thực hiện"