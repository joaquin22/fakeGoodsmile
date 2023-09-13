import pytest
import logging
import json

from django.urls import reverse_lazy

from model_bakery import baker
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

    def test_create(
        self, api_client, create_user_admin, login_user_admin_payload
    ) -> None:
        """
        Test the create manufacture Endpoint
        :param api_client:
        :return: None
        """
        logger.info(f"=====   Start Test Endpoint: Manufacturer Create   =====")

        response_login = api_client().post(
            reverse_lazy("API:login"), data=login_user_admin_payload, format="json"
        )

        logger.info(f"Response Login: {json.loads(response_login.content)}")

        assert json.loads(response_login.content)["id"] == create_user_admin.id
        assert response_login.status_code == status.HTTP_200_OK

        access_token = json.loads(response_login.content)["access"]
        header = {"Authorization": f"Jwt {access_token}"}

        manufacturer = baker.prepare(Manufacturer)
        expected_json = {"name": manufacturer.name}

        logger.info(f"Expected json: {expected_json}")

        response = api_client().post(
            self.endpoint, data=expected_json, format="json", headers=header
        )
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

    def test_put(self, api_client) -> None:
        """
        Test the update manufacture Endpoint
        :param api_client:
        :return: None
        """
        logger.info(f"=====   Start Test Manufacturer Put   =====")

        manufacturer = baker.make(Manufacturer)
        logger.info(f"Manufacturer Name: {manufacturer.name}")

        put_json = {"name": "test"}
        url = f"{self.endpoint}{manufacturer.id}/"
        response = api_client().put(url, put_json)

        logger.info(f"Response: {json.loads(response.content)}")

        assert response.status_code == status.HTTP_200_OK
        assert json.loads(response.content)["name"] == put_json["name"]

        logger.info(f"=====   End Test Manufacturer Put   =====")

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
