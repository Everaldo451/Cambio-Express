from authe.form import RegisterForm, UserRegisterExtras
from django.db import transaction, IntegrityError
from api.models import Company
import pytest

@pytest.fixture
def company_model():
    return Company

@pytest.fixture
def user_data():
    return {
        "email": "valid@gmail.com",
        "full_name": "Any Name",
        "password": "validPassword"
    }

@pytest.fixture
def company_data():
    return {
        "CNPJ": "0200000001",
        "name": "Any C",
        "is_company": "on",
    }

@pytest.fixture
def endpoint():
    return "/auth/register/"


########USER CREATION

@pytest.fixture
def create_user(django_user_model, user_data):
    try:
        user = django_user_model.objects.create_user(
            email=user_data.get("email"),
            password=user_data.get("password")
        )
        return user
    
    except: return None


@pytest.fixture
def create_company(django_user_model, company_model, user_data, company_data):

    try:
        user = None
        company = None
        with transaction.atomic():
            user = django_user_model.objects.create_user(
				email = user_data.get("email"),
				password = user_data.get("password")
			)
            company_data.pop("is_company")
            company = company_model(**company_data, user = user)
            company.save()

        return user, company
    except IntegrityError as e:
        return None, None


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

