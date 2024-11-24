from authe.form import RegisterFormForCompany, RegisterFormForUser
import pytest

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
def create_company_user(user_data):
    pass

@pytest.fixture
def create_company(user_data):
    pass


@pytest.mark.django_db
def test_with_user_is_company(company_form, create_company_user,  create_company):

    user = create_company_user
    company = create_company

    assert company_form
    assert user is not None
    assert company is not None
