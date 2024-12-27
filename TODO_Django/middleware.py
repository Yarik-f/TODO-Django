from django.contrib import messages
from django.utils.timezone import now
from todo.models import Notification

class AdminNotificationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/') and request.user.is_staff:
            notif = Notification.objects.all()
            for n in notif:
                # if n.read:
                #     n.delete()
                # else:
                messages.warning(
                    request,
                    f"Есть {n.task} время выполнения которой подходит к концу."
                )

        response = self.get_response(request)
        return response
