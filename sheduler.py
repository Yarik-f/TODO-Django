# import os
# import django
# import threading
# import schedule
# import time
#
#
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TODO_Django.settings')
# django.setup()
#
from todo.models import Task, Notification
# from django.utils.timezone import now, timedelta
# from django.contrib import messages
from todo.utils import *
# from django.contrib.admin.models import LogEntry, CHANGE
# from django.contrib.contenttypes.models import ContentType
# def check_task_time():
#     current_time = now()
#     tasks = Task.objects.filter(status=False)
#
#     for task in tasks:
#         time_difference = task.date_completed - current_time
#         if timedelta(hours=1) >= time_difference >= timedelta(0):
#             # Отправка уведомления в панель админа
#             Notification.objects.create(task=task)
#             print('Уведомление созданно')
#
#             # Отправка на почту сообщением
#             # subject = f'Задачу "{task.title}" нужно выполнить до {task.date_completed}'
#             # message = f'Описание задачи {task.description}'
#             # print(task.user.email)
#             # send_email_notification(task.user.email, subject, message)
#
#             # Отправка на почту html-страницей
#             # html_content = f"""
#             # <h1>Задачу "{task.title}" нужно выполнить до {task.date_completed}</h1>
#             # <p>Описание задачи {task.description}</p>
#             # """.format(title=task.title, description=task.description)
#             # send_html_email(task.user.email, html_content)
#
# # def check_tasks_and_notify():
# #     current_time = now()
# #     upcoming_tasks = Task.objects.filter(
# #         status=False,
# #         date_completed__lte=current_time + timedelta(hours=1),
# #         date_completed__gte=current_time,
# #     )
# #
# #     for task in upcoming_tasks:
# #         # Создаем уведомление в логах админки
# #         LogEntry.objects.log_action(
# #             user_id=1,  # ID администратора
# #             content_type_id=ContentType.objects.get_for_model(Task).id,
# #             object_id=task.id,
# #             object_repr=str(task),
# #             action_flag=CHANGE,
# #             change_message=f"Задача '{task.title}' скоро должна быть выполнена!"
# #         )
# def run_schedule():
#     while True:
#         schedule.run_pending()
#         time.sleep(1)
#
#
# schedule.every(20).seconds.do(check_task_time)
#
#
# scheduler_thread = threading.Thread(target=run_schedule, daemon=True)
# scheduler_thread.start()
#
# while True:
#     time.sleep(10)
#     print('1')
