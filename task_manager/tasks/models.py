from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from task_manager.labels.models import Label
from task_manager.statuses.models import Status

# Create your models here.


class Task(models.Model):
    name = models.CharField(
        max_length=150, unique=True, verbose_name=_("Name")
    )
    description = models.TextField(blank=True, verbose_name=_("Description"))
    status = models.ForeignKey(
        Status, on_delete=models.PROTECT, null=True, verbose_name=_("Status")
    )
    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name="task_creator",
        verbose_name=_("Creator"),
    )
    executor = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="task_executor",
        verbose_name=_("Executor"),
    )

    created_at = models.DateTimeField(auto_now_add=True)
    labels = models.ManyToManyField(
        Label, blank=True, verbose_name=_("Labels")
    )

    def __str__(self):
        return self.name
