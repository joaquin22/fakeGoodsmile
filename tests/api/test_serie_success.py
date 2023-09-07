import pytest
import logging
import json
from model_bakery import baker


from rest_framework import status

from API.models import Serie

logger = logging.getLogger(__name__)
pytestmark = pytest.mark.django_db


class TestSerieEndpoints:
    endpoint = "/api/serie/"
    logger.info(f"=====   Start Test Serie Endpoints   =====")

    def test_list(self, api_client) -> None:
        """
        Test the list serie Endpoint
        :param api_client:
        :return: None
        """
        logger.info(f"=====   Start Test Serie List   =====")
        baker.make(Serie, _quantity=3)

        response = api_client().get(self.endpoint)
        logger.info(f"Response: {json.loads(response.content)}")

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == 3
        logger.info(f"=====   End Test Serie List   =====")

    def test_create(self, api_client) -> None:
        """
        Test the create serie Endpoint
        :param api_client:
        :return: None
        """
        logger.info(f"=====   Start Test Serie Create   =====")

        serie = baker.prepare(Serie)
        expected_json = {"name": serie.name}

        logger.info(f"Expected json: {expected_json}")

        response = api_client().post(self.endpoint, data=expected_json, format="json")
        serie_id = response.data["id"]

        logger.info(f"Created serie with id: {serie_id}")
        logger.info(f"Response: {json.loads(response.content)}")

        assert response.status_code == status.HTTP_201_CREATED
        assert json.loads(response.content)["name"] == expected_json["name"]

        logger.info(f"=====   EndTest Serie Create   =====")

    def test_retrieve(self, api_client) -> None:
        """
        Test the retrieve serie Endpoint
        :param api_client:
        :return: None
        """
        logger.info(f"=====   Start Test Serie Retrive   =====")

        serie = baker.make(Serie)
        logger.info(f"Serie ID: {serie.id}")
        url = f"{self.endpoint}{serie.id}/"
        response = api_client().get(url)

        logger.info(f"Response: {json.loads(response.content)}")

        assert response.status_code == status.HTTP_200_OK
        assert json.loads(response.content)["name"] == serie.name

        logger.info(f"=====   End Test Serie Retrive   =====")

    def test_put(self, api_client) -> None:
        """
        Test the update serie Endpoint
        :param api_client:
        :return: None
        """
        logger.info(f"=====   Start Test Serie Put   =====")

        serie = baker.make(Serie)
        logger.info(f"Serie Name: {serie.name}")

        put_json = {"name": "test"}
        url = f"{self.endpoint}{serie.id}/"
        response = api_client().put(url, put_json)

        logger.info(f"Response: {json.loads(response.content)}")

        assert response.status_code == status.HTTP_200_OK
        assert json.loads(response.content)["name"] == put_json["name"]

        logger.info(f"=====   End Test Serie Put   =====")

    def test_delete(self, api_client) -> None:
        """
        Test the delete serie Endpoint
        :param api_client:
        :return: None
        """
        logger.info(f"=====   Start Test Serie Delete   =====")

        serie = baker.make(Serie)
        logger.info(f"Serie ID: {serie.id}")
        url = f"{self.endpoint}{serie.id}/"
        response = api_client().delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT

        logger.info(f"=====   End Test Serie Delete   =====")
