from django.db import models

class TaskTag(models.Model):
    tegId = models.IntegerField(auto_created=True, primary_key=True, serialize=True, default=0)
    tegTitle = models.CharField(max_length=100)

    def __str__(self):
        return self.tegTitle

class Task(models.Model):
    taskId = models.IntegerField(auto_created=True, primary_key=True, serialize=True, default=0)
    taskTitle = models.CharField(max_length=100)
    taskTag = models.ForeignKey(TaskTag, on_delete=models.CASCADE)
    taskDescription = models.TextField()

    def __str__(self):
        return f'Task: {self.taskTitle}'

