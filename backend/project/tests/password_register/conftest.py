from authe.form import RegisterForm, CompanyRegisterExtras, UserRegisterExtras
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
        "CNPJ": "0000000000",
        "name": "Any Company",
        "is_company": "on",
    }


########TEST COMPANY USER

@pytest.fixture
def create_user(django_user_model, user_data):

    user = django_user_model.objects.filter(email=user_data.get("email"))
    if user: return "have user"
    try:

        user = django_user_model.objects.create_user(
            email=user_data.get("email"),
            password=user_data.get("password")
        )
        return user
    
    except: return None


@pytest.fixture
def create_same_user(django_user_model,user_data):

    user = django_user_model.objects.create_user(
        email="othervalid@gmail.com",
        password=user_data.get("password")
    )
    return user


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
        return None


@pytest.fixture
def create_same_company(create_same_user, company_model, user_data):

    company = company_model(
        name = user_data.get("name"),
        CNPJ = "00000001",
        user = create_same_user
    )
    company.save()
    return create_same_user, company


@pytest.mark.django_db
def test_user_company(company_form, create_same_company, verify_user, create_company, user_data):

    assert company_form
    assert verify_user is None
    assert create_company is not None
    user, company = create_company
    assert company.CNPJ == user_data.get("CNPJ")
    assert company.name == user_data.get("name")


########TEST PERSON USER

@pytest.fixture
def person_form(user_data):
    return UserRegisterExtras(user_data).is_valid() and RegisterForm(user_data).is_valid()

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

@pytest.fixture
def create_person(django_user_model, user_data, splited_name):
    pass

@pytest.fixture
def create_same_person(django_user_model, user_data, splited_name):

    if not splited_name: return None
    first_name, last_name = splited_name

    user = django_user_model.objects.create_user(
        email= user_data.get("email"),
        password = user_data.get("password"),
        first_name = first_name,
        last_name = last_name
    )
    return user


@pytest.mark.django_db
def test_user_person(person_form, create_same_person, create_person, splited_name):

    assert person_form
    assert not splited_name
    """
    first_name, last_name = firstNameLastName
    assert first_name == "Algum"
    assert last_name == "Nome"
    """
    assert not create_same_person

