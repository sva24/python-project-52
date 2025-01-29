import json

import pytest
from django.contrib.messages import get_messages
from django.urls import reverse

from task_manager.labels.models import Label
from task_manager.users.tests import login, test_user


@pytest.fixture
def test_label(db):
    with open("task_manager/fixtures/labels.json", "r") as file:
        label_data = json.load(file)[0]

    label = Label.objects.create(**label_data)
    return label


@pytest.mark.django_db
def test_label_create(client, test_user, login):
    label_data = {
        "name": "New",
    }

    response = client.post(reverse("label_create"), data=label_data)
    assert response.status_code == 302
    messages = list(get_messages(response.wsgi_request))
    assert str(messages[0]) == "The label was successfully created."

    new_label = Label.objects.get(name=label_data["name"])
    assert new_label.name == label_data["name"]


@pytest.mark.django_db
def test_label_update(client, test_label, test_user, login):
    label_data = {
        "name": "Old",
    }

    url = reverse("label_update", kwargs={"pk": test_label.id})

    response = client.post(url, data=label_data)

    assert response.status_code == 302

    updated_label = Label.objects.get(name=label_data["name"])
    assert updated_label.name == label_data["name"]

    messages = list(get_messages(response.wsgi_request))
    assert str(messages[0]) == "The label has been changed successfully."


@pytest.mark.django_db
def test_labels_list_view(client, test_user, test_label, login):
    url = reverse("labels")
    response = client.get(url)

    assert response.status_code == 200
    assert test_label.name in response.content.decode()


@pytest.mark.django_db
def test_label_delete(client, test_user, test_label, login):
    url = reverse("label_delete", kwargs={"pk": test_label.id})
    response = client.post(url)

    assert response.status_code == 302

    assert not Label.objects.filter(id=test_label.id).exists()
    messages = list(get_messages(response.wsgi_request))
    assert str(messages[0]) == "The label has been successfully removed"
