import pytest
from rest_framework.test import APIClient

from df_remote_config.models import ConfigPart

pytestmark = pytest.mark.django_db


def test_remote_config_returns_200(client: APIClient) -> None:
    ConfigPart.objects.create(name="legal", json={"message": "test"})

    response = client.get("/api/v1/remoteconfig/?part=legal")

    assert response.status_code == 200
    assert response.json() == {"message": "test"}
