from django.contrib import admin, messages
from .models import *

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'description', 'date_completed', 'status', 'is_public')
    actions = ['mark_as_completed']



    def mark_as_completed(self, request, queryset):
        updated = queryset.update(status=True)
        self.message_user(
            request,
            f'{updated} задач(а) успешно отмечены как выполненные.',
            messages.SUCCESS
        )

    mark_as_completed.short_description = "Отметить задачи как выполненные"
