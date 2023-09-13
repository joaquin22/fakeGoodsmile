import pytest
import logging
import json

from rest_framework import status

from API.models import User

logger = logging.getLogger(__name__)
pytestmark = pytest.mark.django_db


class TestAuthEnpoints:
    endpoint = "/api/auth"
    logger.info(f"=====   Start Test: Auth Endpoints   =====")

    def test_login_client_user(
        self, login_user_payload, create_user, api_client
    ) -> None:
        """
        Test the client user login
        Args:
            @api_client: APIClient
            @login_user_payload: Object
                Provide the user info for login (username, password)
            @create_user: model.User
                New user
        """
        logger.info(f"=====   Start Test Endpoint: User Login   =====")
        logger.info(f"User login Request {login_user_payload}")
        logger.info(f"User Info  {create_user.__dict__}")

        # Obtain user access upon successful login.
        response = api_client().post(
            f"{self.endpoint}/login/", data=login_user_payload, format="json"
        )

        logger.info(f"Response: {json.loads(response.content)}")

        # Validate the data if the response is correct
        assert json.loads(response.content)["id"] == create_user.id
        assert response.status_code == status.HTTP_200_OK

        logger.info(f"=====   End Test Endpoint: User Login   =====")

    def test_login_admin_user(
        self, login_user_admin_payload, create_user_admin, api_client
    ) -> None:
        """
        Test the admin login Endpoint
        :param api_client:
        :return: None
        """
        logger.info(f"=====   Start Test Endpoint: Admin Login   =====")
        logger.info(f"User login Request {login_user_admin_payload}")
        logger.info(f"User Info  {create_user_admin.__dict__}")
        response = api_client().post(
            f"{self.endpoint}/login/", data=login_user_admin_payload, format="json"
        )

        logger.info(f"Response: {json.loads(response.content)}")

        assert json.loads(response.content)["id"] == create_user_admin.id
        assert response.status_code == status.HTTP_200_OK

        logger.info(f"=====   End Test Endpoint: Admin Login   =====")

    def test_register_client_user(self, api_client) -> None:
        """
        Test the user register Endpoint
        :param api_client:
        :return: None
        """
        logger.info(f"=====   Start Test Endpoint: User Register    =====")

        register_user_payload = {
            "first_name": "prueba",
            "last_name": "prueba",
            "email": "prueba@mail.com",
            "password": "3volution",
        }

        logger.info(f"User register payload {register_user_payload}")

        response = api_client().post(
            f"{self.endpoint}/register/", data=register_user_payload, format="json"
        )

        logger.info(f"Response: {json.loads(response.content)}")

        assert (
            json.loads(response.content)["data"]["email"]
            == register_user_payload["email"]
        )
        assert response.status_code == status.HTTP_201_CREATED

        logger.info(f"=====   End Test Endpoint: User Register    =====")

    def test_register_admin_user(self, api_client) -> None:
        """
        Test the user register Endpoint
        :param api_client:
        :return: None
        """
        logger.info(f"=====   Start Test Endpoint: Admin Register    =====")

        register_user_payload = {
            "first_name": "prueba",
            "last_name": "prueba",
            "email": "prueba@mail.com",
            "password": "3volution",
            "user_type": "ADMIN",
        }

        logger.info(f"User register payload {register_user_payload}")

        response = api_client().post(
            f"{self.endpoint}/register/", data=register_user_payload, format="json"
        )

        logger.info(f"Response: {json.loads(response.content)}")

        assert (
            json.loads(response.content)["data"]["email"]
            == register_user_payload["email"]
        )
        assert response.status_code == status.HTTP_201_CREATED

        logger.info(f"=====   End Test Endpoint: Admin Register    =====")
