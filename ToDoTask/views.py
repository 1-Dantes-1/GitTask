from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from ToDoTask.models import Task, TaskTag
from ToDoTask.serializers import TaskSerializer, TaskTagSerializer

class TaskAPIView(APIView):
    def get(self, request: Request):
        c = Task.objects.filter(
            taskId=request.query_params['taskId']
        )
        return Response({'tasks': TaskSerializer(c, many=True).data})

    def post(self, request):
        ser = TaskSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        taskTag = get_object_or_404(TaskTag, pk=request.data.get("taskTag"))
        task_new = Task.objects.create(
            taskTitle=request.data['taskTitle'],
            taskDescription=request.data['taskDescription'],
            taskTag=taskTag
        )
        return Response({'tasks': TaskSerializer(task_new).data})

class TagAPIView(APIView):
    def get(self, request):
        t = Task.objects.all().filter(
            taskTag_id=request.query_params['tegId']
        )
        return Response({"tags": TaskSerializer(t, many=True).data})

    def post(self, request):
        ser = TaskTagSerializer(data=request.data)
        ser.is_valid(raise_exception=True)

        tag_new = TaskTag.objects.create(
            tegTitle=request.data['tegTitle']
        )
        return Response({'tags': TaskTagSerializer(tag_new).data})

