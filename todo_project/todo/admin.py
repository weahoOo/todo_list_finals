from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_done', 'created_at')  # Updated
    list_filter = ('is_done', 'created_at')  # 'is_completed' is valid in list_filter

    # Add a custom method to display the boolean field in list_display
    @admin.display(boolean=True, description='Completed')
    def is_completed_display(self, obj):
        return obj.is_completed
