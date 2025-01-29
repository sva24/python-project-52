import json

import pytest
from django.contrib.messages import get_messages
from django.urls import reverse

from task_manager.labels.tests import test_label
from task_manager.statuses.tests import test_status
from task_manager.tasks.models import Task
from task_manager.users.tests import login, test_user


@pytest.fixture
def test_task(db, test_user, test_status, test_label):
    with open("task_manager/fixtures/tasks.json", "r") as file:
        task_data = json.load(file)[0]

    task_data["status"] = test_status
    task_data["created_by"] = test_user
    task_data["executor"] = test_user

    task = Task.objects.create(**task_data)
    task.labels.add(test_label)
    return task


@pytest.mark.django_db
def test_task_create(client, test_user, login, test_status, test_label):
    task_data = {
        "name": "New Task",
        "description": "Another new task",
        "status": test_status.id,
        "created_by": test_user.id,
        "executor": test_user.id,
    }

    response = client.post(reverse("task_create"), data=task_data)
    assert response.status_code == 302
    messages = list(get_messages(response.wsgi_request))
    assert str(messages[0]) == "Task successfully created"

    new_task = Task.objects.get(name=task_data["name"])
    assert new_task.name == task_data["name"]


@pytest.mark.django_db
def test_task_update(
    client, test_task, test_user, login, test_status, test_label
):
    task_data = {
        "name": "Updated Task",
        "description": "Updated task.",
        "status": test_status.id,
        "executor": test_user.id,
    }

    url = reverse("task_update", kwargs={"pk": test_task.id})

    response = client.post(url, data=task_data)

    assert response.status_code == 302

    updated_task = Task.objects.get(name=task_data["name"])
    assert updated_task.name == task_data["name"]
    assert updated_task.description == task_data["description"]
    assert updated_task.status.id == task_data["status"]

    messages = list(get_messages(response.wsgi_request))
    assert str(messages[0]) == "Task successfully updated"


@pytest.mark.django_db
def test_tasks_list_view(client, test_user, test_task, login):
    url = reverse("tasks")
    response = client.get(url)

    assert response.status_code == 200
    assert test_task.name in response.content.decode()


@pytest.mark.django_db
def test_task_delete(client, test_user, test_task, login):
    url = reverse("task_delete", kwargs={"pk": test_task.id})
    response = client.post(url)

    assert response.status_code == 302

    assert not Task.objects.filter(id=test_task.id).exists()
    messages = list(get_messages(response.wsgi_request))
    assert str(messages[0]) == "Task successfully deleted"
