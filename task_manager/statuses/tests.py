import json

import pytest
from django.contrib.messages import get_messages
from django.urls import reverse

from task_manager.statuses.models import Status
from task_manager.users.tests import login, test_user


@pytest.fixture
def test_status(db):
    with open("task_manager/fixtures/statuses.json", "r") as file:
        status_data = json.load(file)[0]

    status = Status.objects.create(**status_data)
    return status


@pytest.mark.django_db
def test_status_create(client, test_user, login):
    status_data = {
        "name": "In work",
    }

    response = client.post(reverse("status_create"), data=status_data)
    assert response.status_code == 302
    messages = list(get_messages(response.wsgi_request))
    assert str(messages[0]) == "Status created successfully"

    new_status = Status.objects.get(name=status_data["name"])
    assert new_status.name == status_data["name"]


@pytest.mark.django_db
def test_status_update(client, test_status, test_user, login):
    status_data = {
        "name": "Closed",
    }

    url = reverse("status_update", kwargs={"pk": test_status.id})

    response = client.post(url, data=status_data)

    assert response.status_code == 302

    updated_status = Status.objects.get(name=status_data["name"])
    assert updated_status.name == status_data["name"]

    messages = list(get_messages(response.wsgi_request))
    assert str(messages[0]) == "Status updated successfully"


@pytest.mark.django_db
def test_statuses_list_view(client, test_user, test_status, login):
    url = reverse("statuses")
    response = client.get(url)

    assert response.status_code == 200
    assert test_status.name in response.content.decode()


@pytest.mark.django_db
def test_status_delete(client, test_user, test_status, login):
    url = reverse("status_delete", kwargs={"pk": test_status.id})
    response = client.post(url)

    assert response.status_code == 302

    assert not Status.objects.filter(id=test_status.id).exists()
    messages = list(get_messages(response.wsgi_request))
    assert str(messages[0]) == "Status successfully deleted"
