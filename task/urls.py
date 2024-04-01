# tasks/urls.py
from django.urls import path
from .views import (
    TaskCreateAPIView,
    TaskCompleteAPIView,
    TaskDeleteAPIView,
    TaskListAPIView,
    CompletedTaskListAPIView,
    UncompletedTaskListAPIView,
)

urlpatterns = [
    path('create/', TaskCreateAPIView.as_view(), name='task-create'),
    path('complete/<int:task_id>/', TaskCompleteAPIView.as_view(), name='task-complete'),
    path('delete/<int:task_id>/', TaskDeleteAPIView.as_view(), name='task-delete'),
    path('list/', TaskListAPIView.as_view(), name='task-list'),
    path('completed/', CompletedTaskListAPIView.as_view(), name='completed-task-list'),
    path('uncompleted/', UncompletedTaskListAPIView.as_view(), name='uncompleted-task-list'),
]
