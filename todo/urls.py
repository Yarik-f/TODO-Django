from django.urls import path, include
from todo import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tasks', views.TaskViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.task_view, name='task_list'),
    path('task/create/', views.create_task, name='task_create'),
    path('task/<int:pk>/delete/', views.delete_task, name='task_delete'),
    path('task/<int:pk>/update/', views.update_task, name='task_update'),
    path('task/<int:pk>/toggle/', views.toggle_task, name='task_toggle'),
]