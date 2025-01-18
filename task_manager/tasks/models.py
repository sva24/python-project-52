from django.db import models
from django.contrib.auth import get_user_model
from task_manager.statuses.models import Status


# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL,
                               null=True,
                               blank=True)
    created_by = models.ForeignKey(get_user_model(),
                                   on_delete=models.CASCADE,
                                   related_name='task_creator')
    executor = models.ForeignKey(get_user_model(),
                                 on_delete=models.SET_NULL,
                                 null=True, blank=True,
                                 related_name='task_executor')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
