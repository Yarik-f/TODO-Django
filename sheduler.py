import os

from django.utils.timezone import now, timedelta

from todo.utils import *
import django
import threading
import schedule
import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TODO_Django.settings')
django.setup()

from todo.models import Task
def check_task_time():
    current_time = now()
    tasks = Task.objects.filter(status=False)

    for task in tasks:
        time_difference = task.date_completed - current_time
        if timedelta(hours=1) >= time_difference >= timedelta(0):
            # subject = f'Задачу "{task.title}" нужно выполнить до {task.date_completed}'
            # message = f'Описание задачи {task.description}'
            # print(task.user.email)
            # send_email_notification(task.user.email, subject, message)

            html_content = f"""
            <h1>Задачу "{task.title}" нужно выполнить до {task.date_completed}</h1>
            <p>Описание задачи {task.description}</p>
            """.format(title=task.title, description=task.description)
            send_html_email(task.user.email, html_content)

def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)


schedule.every(20).seconds.do(check_task_time)


scheduler_thread = threading.Thread(target=run_schedule, daemon=True)
scheduler_thread.start()

while True:
    time.sleep(10)
    print('1')
