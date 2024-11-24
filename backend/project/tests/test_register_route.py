from authe.form import RegisterFormForCompany, RegisterFormForUser
from api.models import Company
import pytest

@pytest.fixture
def company_model():
    return Company

@pytest.fixture
def user_data():
    return {
        "ema": "emailinvalido",
        "password": "senhaValida",
        "CNPJ": "0000000000",
        "name": "Alguma Empresa",
        "is_company": "on"
    }

@pytest.fixture
def company_form(user_data):
    return RegisterFormForCompany(user_data).is_valid()

@pytest.fixture
def person_form(user_data):
    return RegisterFormForUser(user_data).is_valid()

@pytest.fixture
def create_user(django_user_model, user_data):

    try :

        user = django_user_model.objects.create_user(
            email=user_data.get("email"),
            password=user_data.get("password")
        )
        return user
    
    except: return None

@pytest.fixture
def create_company(create_user, company_model, user_data):

    try:

        company = company_model(
            name = user_data.get("name"),
            CNPJ = user_data.get("CNPJ"),
            user = create_user
        )
        company.save()
        return create_user, company
    
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
        user = create_same_user
    )
    company.save()
    return create_same_user, company


@pytest.mark.django_db
def testUserCompany(company_form, create_company):

    assert not company_form
    assert create_company is None

"""

@pytest.fixture
def firstNameLastName(user_data):
    full_name = user_data.get("full_name")

    splited = full_name.split(maxsplit=1)
    first_name  = splited[0]
    last_name = splited[1]
    return first_name, last_name

@pytest.fixture
def create_same_person(django_user_model, user_data, firstNameLastName):

    user = django_user_model.objects.create_user(
        email= user_data.get("email"),
        password = user_data.get("password")
    )

@pytest.mark.django_db
def testUserPerson(person_form, create_same_person, create_person):

    assert person_form
    assert create_person is None
    

#same_user, same_company = create_same_company

#user, company = create_company


"""