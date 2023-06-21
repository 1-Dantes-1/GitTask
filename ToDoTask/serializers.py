from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.renderers import JSONRenderer

class TaskSerializer(serializers.Serializer):
    taskId = serializers.IntegerField()
    taskTitle = serializers.CharField()
    taskTag = serializers.CharField()
    taskDescription = serializers.CharField()

class TaskTagSerializer(serializers.Serializer):
    tegId = serializers.IntegerField()
    tegTitle = serializers.CharField()
