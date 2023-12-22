import uuid

import pytest
from django.contrib.auth.models import User
from django.core.cache import cache
from rest_framework.test import APIClient

from config import settings
from constants import LOGIN_USER


@pytest.fixture
def first_user():
    return User.objects.create(username='first_user', password="12345")


def set_token(client):
    user = User.objects.first()
    token = uuid.uuid4().hex
    cache.set(
        LOGIN_USER.format(token=token, project_name=settings.PROJECT_NAME),
        user.pk,
    )
    client.cookies.set("access_token", token)


@pytest.fixture(scope="function")
def client(first_user):
    async with APIClient() as client:
        set_token(client)
        yield client
