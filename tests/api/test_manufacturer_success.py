import pytest
import logging

from rest_framework.test import APIClient
from rest_framework import status

client = APIClient()
logger = logging.getLogger(__name__)


@pytest.mark.django_db
def test_list_manufacturers():
    response = client.get("/api/manufacturer/")
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_create_manufacturer(api_client) -> None:
    """
    Test the create task API
    :param api_client:
    :return: None
    """
    payload = {
        "name": "Good Smie Fake",
    }

    # Create a task
    response_create = api_client.post("/api/manufacturer/", data=payload, format="json")

    manufacturer_id = response_create.data["id"]
    logger.info(f"Created manufacturer with id: {manufacturer_id}")
    logger.info(f"Response: {response_create.data}")
    assert response_create.status_code == 201
    assert response_create.data["name"] == payload["name"]

    # Read the task
    response_read = api_client.get(
        f"/api/manufacturer/{manufacturer_id}/", format="json"
    )
    logger.info(f"Read manufacturer with id: {manufacturer_id}")
    logger.info(f"Response: {response_read.data}")
    assert response_read.status_code == 200
    assert response_read.data["name"] == payload["name"]
