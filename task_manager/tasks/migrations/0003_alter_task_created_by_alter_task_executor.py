# Generated by Django 5.1.3 on 2025-01-23 07:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_task_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='task_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='executor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='task_executor', to=settings.AUTH_USER_MODEL),
        ),
    ]
