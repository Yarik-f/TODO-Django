from django.urls import path, include
from todo import views
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views

router = DefaultRouter()
router.register('tasks', views.TaskViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.task_view, name='task_list'),
    path('task/create/', views.create_task, name='task_create'),
    path('task/test/', views.test_view, name='task_test'),
    path('task/<int:pk>/delete/', views.delete_task, name='task_delete'),
    path('task/<int:pk>/update/', views.update_task, name='task_update'),
    path('task/<int:pk>/toggle/', views.toggle_task, name='task_toggle'),
    path('account/', views.account_view, name='account'),
    path('account/register/', views.register_view, name='register'),
    path('account/login/', auth_views.LoginView.as_view(template_name='profile/login.html'), name='login'),
    path('account/logout/', auth_views.LogoutView.as_view(next_page='task_list'), name='logout'),
    # path('check-notifications/', views.check_notifications, name='check_notifications'),
]
