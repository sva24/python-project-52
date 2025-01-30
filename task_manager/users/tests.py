import pytest
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from django.urls import reverse


@pytest.mark.django_db
def test_user_create(client):
    user_data = {
        "username": "TestUser",
        "first_name": "Ivan",
        "last_name": "Ivanov",
        "password1": "123456",
        "password2": "123456",
    }

    response = client.post(reverse("sign_up"), data=user_data)
    assert response.status_code == 302
    messages = list(get_messages(response.wsgi_request))
    assert str(messages[0]) == "User created successfully"

    new_user = get_user_model().objects.get(username=user_data["username"])
    assert new_user.first_name == user_data["first_name"]
    assert new_user.last_name == user_data["last_name"]


@pytest.mark.django_db
def test_user_update(client, test_user, login):
    update_data = {
        "first_name": "Sergei",
        "last_name": "Petrov",
        "username": test_user.username,
        "password1": "123",
        "password2": "123",
    }

    url = reverse("user_update", kwargs={"pk": test_user.id})
    response = client.post(url, data=update_data)

    assert response.status_code == 302

    updated_user = get_user_model().objects.get(id=test_user.id)
    assert updated_user.first_name == update_data["first_name"]
    assert updated_user.last_name == update_data["last_name"]

    messages = list(get_messages(response.wsgi_request))
    assert str(messages[0]) == "User was updated successfully"


@pytest.mark.django_db
def test_user_update_other_user(client, test_user, login):
    other_user = get_user_model().objects.create_user(
        username="otheruser",
        password="testpassword123",
    )
    url = reverse("user_update", kwargs={"pk": other_user.id})
    response = client.post(url, data={})
    assert response.status_code == 302
    messages = list(get_messages(response.wsgi_request))
    assert (
        str(messages[0])
        == "You do not have permission to change another user."
    )


@pytest.mark.django_db
def test_user_update_unauthenticated(client, test_user):
    url = reverse("user_update", kwargs={"pk": test_user.id})
    response = client.post(url, data={})
    assert response.status_code == 302
    messages = list(get_messages(response.wsgi_request))
    assert str(messages[0]) == "You are not logged in! Please sign in."


@pytest.mark.django_db
def test_users_list_view(client, test_user):
    url = reverse("users")
    response = client.get(url)
    assert response.status_code == 200
    assert test_user.username in response.content.decode()


@pytest.mark.django_db
def test_user_delete(client, test_user, login):
    url = reverse("user_delete", kwargs={"pk": test_user.id})
    response = client.post(url)

    assert response.status_code == 302

    with pytest.raises(get_user_model().DoesNotExist):
        get_user_model().objects.get(id=test_user.id)
    messages = list(get_messages(response.wsgi_request))
    assert str(messages[0]) == "User successfully deleted"


@pytest.mark.django_db
def test_user_delete_other_user(client, test_user, login):
    other_user = get_user_model().objects.create_user(
        username="otheruser",
        password="testpassword123",
    )

    url = reverse("user_delete", kwargs={"pk": other_user.id})
    response = client.post(url)

    assert response.status_code == 302
    assert get_user_model().objects.filter(id=other_user.id).exists()

    messages = list(get_messages(response.wsgi_request))
    print(messages)
    assert (
        str(messages[0])
        == "You do not have permission to change another user."
    )


@pytest.mark.django_db
def test_user_delete_view_unauthenticated(client, test_user):
    url = reverse("user_delete", kwargs={"pk": test_user.id})
    response = client.post(url)

    assert response.status_code == 302
    assert get_user_model().objects.filter(id=test_user.id).exists()

    messages = list(get_messages(response.wsgi_request))
    assert str(messages[0]) == "You are not logged in! Please sign in."
