import pytest
from API.choices import UserTypeChoices
from API.models import User


# CLIENT USER
@pytest.fixture
def create_user():
    user = User.objects.create(
        first_name="Joaquin",
        last_name="Huaman",
        username="fake@mail.com",
        email="fake@mail.com",
        user_type=UserTypeChoices.USER,
    )

    user.set_password("password")
    user.save()

    return user


@pytest.fixture
def login_user_payload():
    return {
        "username": "fake@mail.com",
        "password": "password",
    }


# ADMIN USER
@pytest.fixture
def create_user_admin():
    user = User.objects.create(
        first_name="Joaquin",
        last_name="Huaman",
        username="admin@mail.com",
        email="admin@mail.com",
        user_type=UserTypeChoices.ADMIN,
    )

    user.set_password("password")
    user.save()

    return user


@pytest.fixture
def login_user_admin_payload():
    return {
        "username": "admin@mail.com",
        "password": "password",
    }
