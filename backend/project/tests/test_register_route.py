from authe.form import RegisterFormForCompany, RegisterFormForUser
from api.models import Company
import pytest

@pytest.fixture
def company_model():
    return Company

@pytest.fixture
def user_data():
    return {
        "email": "email@valido.com",
        "password": "senhaValida",
        "CNPJ": "0000000000",
        "name": "Alguma Empresa",
        "is_company": "on"
    }

@pytest.fixture
def company_form(user_data):
    return RegisterFormForCompany(user_data).is_valid


@pytest.fixture
def create_user(django_user_model,user_data):

    try :

        user = django_user_model.objects.create_user(
            email=user_data.get("email"),
            password=user_data.get("password")
        )
        return user
    
    except: return None

@pytest.fixture
def create_company(company_model, user_data):

    try:

        company = company_model(
            name = user_data.get("name"),
            CNPJ = user_data.get("CNPJ"),
        )
        company.save()
        return company
    
    except: return None


@pytest.fixture
def create_same_user(django_user_model,user_data):
    user = django_user_model.objects.create_user(
        email=user_data.get("email"),
        password=user_data.get("password")
    )
    return user

@pytest.fixture
def create_same_company(create_same_user, company_model, user_data):
    company = company_model(
        name = user_data.get("name"),
        CNPJ = user_data.get("CNPJ"),
    )
    company.save()
    return company


@pytest.mark.django_db
def testUserCompany(company_form, create_same_company, create_user,  create_company,):

    assert company_form
    assert create_user is None
    assert create_company is None
