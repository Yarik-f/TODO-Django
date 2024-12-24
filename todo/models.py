from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    status = models.BooleanField(default=False)
    date_completed = models.DateTimeField()

    def __str__(self):
        return f'{self.title} | {self.status}'
