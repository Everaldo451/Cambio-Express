from django.db import transaction, IntegrityError
from users.serializers.models.user import UserSerializer
from rest_framework.test import APIRequestFactory
import pytest

@pytest.fixture
def company_model():
    return Company

@pytest.fixture
def user_data():
    return {
        "email": "valid@gmail.com",
        "first_name": "Any",
        "last_name": "Name",
        "password": "validPassword"
    }

@pytest.fixture
def company_data():
    return {
        "CNPJ": "02000000000001",
        "name": "Any C",
    }

@pytest.fixture
def endpoint():
    return "/api/v1/users/"


########USER CREATION

@pytest.fixture
def create_user(endpoint, user_data):
    factory = APIRequestFactory()
    request = factory.post(
        endpoint, 
        {
            **user_data,
        },
        format='json'
    )

    serializer = UserSerializer(
        data={**user_data},
        context={'request':request}
    )
    serializer.is_valid()
    return serializer.save()

@pytest.fixture
def create_company(endpoint, user_data, company_data):
    factory = APIRequestFactory()
    request = factory.post(
        endpoint, 
        {**user_data},
        format='json'
    )
    serializer = UserSerializer(
        data={
            **user_data,
            'company': {
                **company_data
            }
        },
        context={'request':request}
    )
    serializer.is_valid()
    user = serializer.save()
    return user, user.company
    """
    try:
        user = None
        company = None
        with transaction.atomic():
            user = django_user_model.objects.create_user(
				email = user_data.get("email"),
				password = user_data.get("password")
			)
            company = company_model(**company_data, user = user)
            company.save()

        return user, company
    except IntegrityError as e:
        return None, None
    """


@pytest.fixture
def splited_name(user_data):
    full_name = user_data.get("full_name")

    try:
        splited = full_name.split(maxsplit=1)
        first_name  = splited[0]
        last_name = splited[1]
        return first_name, last_name
    except IndexError:
        return None

