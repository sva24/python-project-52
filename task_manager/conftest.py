import json

import pytest
from django.contrib.auth import get_user_model

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task


@pytest.fixture
def login(client):
    with open("task_manager/fixtures/users.json", "r") as file:
        user_data = json.load(file)[0]

    client.login(
        username=user_data["username"], password=user_data["password"]
    )
    return client


@pytest.fixture
def test_user(db):
    with open("task_manager/fixtures/users.json", "r") as file:
        user_data = json.load(file)[0]

    user = get_user_model().objects.create_user(
        username=user_data["username"],
        first_name=user_data["first_name"],
        last_name=user_data["last_name"],
        password=user_data["password"],
    )
    return user


@pytest.fixture
def test_label(db):
    with open("task_manager/fixtures/labels.json", "r") as file:
        label_data = json.load(file)[0]

    label = Label.objects.create(**label_data)
    return label


@pytest.fixture
def test_status(db):
    with open("task_manager/fixtures/statuses.json", "r") as file:
        status_data = json.load(file)[0]

    status = Status.objects.create(**status_data)
    return status


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
