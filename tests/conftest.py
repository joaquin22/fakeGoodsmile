import pytest

from rest_framework.test import APIClient

pytest_plugins = [
    "tests.fixtures.fixture_auth",
]


@pytest.fixture
def api_client() -> APIClient:
    """
    Fixture to provide an API client
    :return: APIClient
    """
    yield APIClient
