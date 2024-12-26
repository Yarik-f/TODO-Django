from django.contrib import messages
from django.utils.timezone import now
from todo.models import Task

class AdminNotificationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/') and request.user.is_staff:
            overdue_tasks = Task.objects.filter(status=False, date_completed__lt=now()).count()
            if overdue_tasks > 0:
                messages.warning(
                    request,
                    f"Есть {overdue_tasks} просроченных задач! Проверьте список."
                )

        response = self.get_response(request)
        return response
