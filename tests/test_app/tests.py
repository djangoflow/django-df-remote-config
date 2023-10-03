import json

import pytest
from rest_framework.test import APIClient

from df_remote_config.models import ConfigAttribute, ConfigPart

pytestmark = pytest.mark.django_db


def test_remote_config_returns_200(client: APIClient) -> None:
    ConfigPart.objects.create(name="legal", json={"message": "test"})

    response = client.get("/api/v1/remoteconfig/?part=legal")

    assert response.status_code == 200
    assert response.json()["data"] == {"message": "test"}


@pytest.mark.parametrize(
    "part_name,attribute_name,attribute_value,search_value,is_success",
    [
        ("legal", "param", "test1", "test1", True),
        ("legal", "param", "test1", "test2", False),
    ],
)
def test_remote_config_attribute_filtering(
    part_name: str,
    attribute_name: str,
    attribute_value: str,
    search_value: str,
    is_success: bool,
    client: APIClient,
) -> None:
    data = {"message": "test"}
    part = ConfigPart.objects.create(name=part_name, json=data)
    attr = ConfigAttribute.objects.create(name=attribute_name, value=attribute_value)
    part.attributes.add(attr)

    response = client.get(
        "/api/v1/remoteconfig/",
        {
            "part": part_name,
            "attributes": json.dumps({attribute_name: search_value}),
        },
    )

    if is_success:
        assert response.status_code == 200
        assert response.json()["data"] == data
    else:
        assert response.status_code == 404
