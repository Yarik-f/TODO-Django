from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='task')
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    status = models.BooleanField(default=False)
    date_completed = models.DateTimeField()
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} | {self.status}'

class Notification(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.task.title}'