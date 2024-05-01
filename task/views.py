# tasks/views.py
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Task
from .serializers import TaskSerializer


class TaskCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def patch(request, task_id):
        try:
            task = Task.objects.get(id=task_id, user=request.user)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

        if task:
            serializer = TaskSerializer(task, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)


class TaskCompleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, task_id):
        try:
            task = Task.objects.get(id=task_id, user=request.user)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

        task.completed = True
        task.save()
        serializer = TaskSerializer(task)
        return Response(serializer.data)


class TaskDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def delete(request, task_id):
        try:
            task = Task.objects.get(id=task_id, user=request.user)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        tasks = Task.objects.filter(user=request.user)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


class CompletedTaskListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        tasks = Task.objects.filter(user=request.user, completed=True)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


class UncompletedTaskListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        tasks = Task.objects.filter(user=request.user, completed=False)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
