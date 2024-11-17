from api.models import User
import pytest

@pytest.fixture
def delete_user(user:User):
    user.delete()

@pytest.fixture
def create_user(delete_user):
    userData = [
        "alguem",
        "algo@gmail.com",
        "algumacoisa",
    ]
    user = User.create_user(**userData)
    yield user
    delete_user(user)