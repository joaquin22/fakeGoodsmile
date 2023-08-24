import pytest
import logging
import json
from model_bakery import baker

from rest_framework.test import APIClient
from rest_framework import status

from API.models import Manufacturer

logger = logging.getLogger(__name__)
pytestmark = pytest.mark.django_db


class TestManufacturerEndpoints:
    endpoint = "/api/manufacturer/"

    logger.info(f"=====   Start Test Manufacturer Endpoints   =====")

    def test_list(self, api_client) -> None:
        """
        Test the list manufactures Endpoint
        :param api_client:
        :return: None
        """
        logger.info(f"=====   Start Test Manufacturer List   =====")
        baker.make(Manufacturer, _quantity=3)

        response = api_client().get(self.endpoint)
        logger.info(f"Response: {json.loads(response.content)}")

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == 3
        logger.info(f"=====   End Test Manufacturer List   =====")

    def test_create(self, api_client) -> None:
        """
        Test the create manufacture Endpoint
        :param api_client:
        :return: None
        """
        logger.info(f"=====   Start Test Manufacturer Create   =====")

        manufacturer = baker.prepare(Manufacturer)
        expected_json = {"name": manufacturer.name}

        logger.info(f"Expected json: {expected_json}")

        response = api_client().post(self.endpoint, data=expected_json, format="json")
        manufacturer_id = response.data["id"]

        logger.info(f"Created manufacturer with id: {manufacturer_id}")
        logger.info(f"Response: {json.loads(response.content)}")

        assert response.status_code == status.HTTP_201_CREATED
        assert json.loads(response.content)["name"] == expected_json["name"]

        logger.info(f"=====   EndTest Manufacturer Create   =====")

    def test_retrieve(self, api_client) -> None:
        """
        Test the retrieve manufacture Endpoint
        :param api_client:
        :return: None
        """
        logger.info(f"=====   Start Test Manufacturer Retrive   =====")

        manufacturer = baker.make(Manufacturer)
        logger.info(f"Manufacturer ID: {manufacturer.id}")
        url = f"{self.endpoint}{manufacturer.id}/"
        response = api_client().get(url)

        logger.info(f"Response: {json.loads(response.content)}")

        assert response.status_code == status.HTTP_200_OK
        assert json.loads(response.content)["name"] == manufacturer.name

        logger.info(f"=====   End Test Manufacturer Retrive   =====")

    def test_delete(self, api_client) -> None:
        """
        Test the delete manufacture Endpoint
        :param api_client:
        :return: None
        """
        logger.info(f"=====   Start Test Manufacturer Delete   =====")

        manufacturer = baker.make(Manufacturer)
        logger.info(f"Manufacturer ID: {manufacturer.id}")
        url = f"{self.endpoint}{manufacturer.id}/"
        response = api_client().delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT

        logger.info(f"=====   End Test Manufacturer Delete   =====")
