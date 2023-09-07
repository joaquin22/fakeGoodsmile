import pytest
import logging
import json
from model_bakery import baker

from django.core.files.uploadedfile import SimpleUploadedFile
from six import BytesIO
from PIL import Image

from rest_framework import status

from API.models import Product, Manufacturer, Serie

logger = logging.getLogger(__name__)
pytestmark = pytest.mark.django_db


class TestProductEndpoints:
    endpoint = "/api/product/"
    logger.info(f"=====   Start Test Product Endpoints   =====")

    def test_list(self, api_client) -> None:
        """
        Test the list products Endpoint
        :param api_client:
        :return: None
        """
        logger.info(f"=====   Start Test Product List   =====")
        baker.make(Product, _quantity=3)

        response = api_client().get(self.endpoint)
        logger.info(f"Response: {json.loads(response.content)}")

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == 3
        logger.info(f"=====   End Test Product List   =====")

    def test_create(self, api_client) -> None:
        """
        Test the list products Endpoint
        :param api_client:
        :return: None
        """
        logger.info(f"=====   Start Test Product Create   =====")
        product = baker.prepare(Product)

        manufacturer = baker.make(Manufacturer)
        logger.info(f"Manufacturer ID: {manufacturer.id}")

        serie = baker.make(Serie)
        logger.info(f"Serie ID: {serie.id}")

        images_list = []

        for _ in range(3):
            size = (800, 600)
            storage = BytesIO()
            img = Image.new("RGB", size)
            img.save(storage, "JPEG")
            storage.seek(0)
            file = SimpleUploadedFile(
                name="test_image.jpg",
                content=storage.getvalue(),
                content_type="image/jpeg",
            )
            images_list.append(file)

        expected_json = {
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "manufacturer": manufacturer.id,
            "serie": serie.id,
            "specifications": product.specifications,
            "release_date": product.release_date,
            "images": images_list,
        }

        logger.info(f"Expected json: {expected_json}")

        response = api_client().post(
            self.endpoint, data=expected_json, format="multipart"
        )

        logger.info(f"Response: {json.loads(response.content)}")

        product_id = response.data["id"]
        logger.info(f"Created product with id: {product_id}")

        assert response.status_code == status.HTTP_201_CREATED
        assert json.loads(response.content)["name"] == expected_json["name"]

        logger.info(f"=====   End Test Product Create   =====")

    def test_retrieve(self, api_client) -> None:
        """
        Test the retrieve product Endpoint
        :param api_client:
        :return: None
        """
        logger.info(f"=====   Start Test Product Retrive   =====")

        product = baker.make(Product)
        logger.info(f"Product ID: {product.id}")
        url = f"{self.endpoint}{product.id}/"
        response = api_client().get(url)

        logger.info(f"Response: {json.loads(response.content)}")

        assert response.status_code == status.HTTP_200_OK
        assert json.loads(response.content)["name"] == product.name

        logger.info(f"=====   End Test Product Retrive   =====")

    def test_patch(self, api_client) -> None:
        """
        Test the update product Endpoint
        :param api_client:
        :return: None
        """
        logger.info(f"=====   Start Test Product Put   =====")

        product = baker.make(Product)
        logger.info(f"Product Name: {product.name}")

        put_json = {"name": "test"}
        url = f"{self.endpoint}{product.id}/"
        response = api_client().patch(url, put_json)

        logger.info(f"Response: {json.loads(response.content)}")

        assert response.status_code == status.HTTP_200_OK
        assert json.loads(response.content)["name"] == put_json["name"]

        logger.info(f"Patch images")

        images_list = []

        for _ in range(3):
            size = (800, 600)
            storage = BytesIO()
            img = Image.new("RGB", size)
            img.save(storage, "JPEG")
            storage.seek(0)
            file = SimpleUploadedFile(
                name="test_image.jpg",
                content=storage.getvalue(),
                content_type="image/jpeg",
            )
            images_list.append(file)

        patch_images_json = {
            "images": images_list,
        }

        response_images = api_client().patch(url, patch_images_json)
        logger.info(f"Response Images: {json.loads(response_images.content)}")

        assert response_images.status_code == status.HTTP_200_OK

        logger.info(f"=====   End Test Product Put   =====")

    def test_delete(self, api_client) -> None:
        """
        Test the delete product Endpoint
        :param api_client:
        :return: None
        """
        logger.info(f"=====   Start Test Product Delete   =====")

        product = baker.make(Product)
        logger.info(f"Product ID: {product.id}")
        url = f"{self.endpoint}{product.id}/"
        response = api_client().delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT

        logger.info(f"=====   End Test Product Delete   =====")
