from django.db import models

from authenticator.models import User

# Create your models here.

class Task_List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_list')
    task_title = models.CharField(max_length=50, blank=False, null=False)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True,null=True)
    def __str__(self):
        return self.task_title

class Tasks(models.Model):
    task_list = models.ForeignKey(Task_List, on_delete=models.CASCADE,related_name="task")
    task_name = models.CharField(max_length=250)
    status_code = models.IntegerField()
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.task_name