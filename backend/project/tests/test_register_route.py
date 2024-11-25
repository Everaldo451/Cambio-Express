from authe.form import RegisterFormForCompany, RegisterFormForUser
from django.db import transaction, IntegrityError
from api.models import Company
import pytest

@pytest.fixture
def company_model():
    return Company

@pytest.fixture
def user_data():
    return {
        "email": "email@invalido.com",
        "password": "senhaValida",
        "CNPJ": "0000000000",
        "name": "Alguma Empresa",
        "is_company": "on"
    }

@pytest.fixture
def company_form(user_data):
    return RegisterFormForCompany(user_data).is_valid()

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
def verify_user(django_user_model, user_data):

    user = django_user_model.objects.filter(email=user_data.get("email"))

    if user: return "have user"

    return None





@pytest.fixture
def create_company(django_user_model, company_model, user_data):

    user = None
    company = None
    try:

        with transaction.atomic():

            user = django_user_model.objects.create_user(
				email = user_data.get("email"),
				password=user_data.get("password")
			)

            company = company_model(

			    name = user_data.get("name"),
			    CNPJ = user_data.get("CNPJ"),
			    user = user
		    )

            company.save()

        return user, company
    
    except IntegrityError as e: 

        return None


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
        CNPJ = "0000001",
        user = create_same_user
    )
    company.save()
    return create_same_user, company


@pytest.mark.django_db
def testUserCompany(company_form, create_same_company, verify_user, create_company):

    assert company_form
    assert verify_user == "have user"
    assert not create_company



@pytest.fixture
def person_form(user_data):
    return RegisterFormForUser(user_data).is_valid()

@pytest.fixture
def firstNameLastName(user_data):
    full_name = user_data.get("full_name")

    if full_name:
        splited = full_name.split(maxsplit=1)
        first_name  = splited[0]
        last_name = splited[1]
        return first_name, last_name

@pytest.fixture
def create_person(django_user_model, user_data, firstNameLastName):
    pass

@pytest.fixture
def create_same_person(django_user_model, user_data, firstNameLastName):

    if not firstNameLastName: return None

    first_name, last_name = firstNameLastName

    user = django_user_model.objects.create_user(
        email= user_data.get("email"),
        password = user_data.get("password"),
        first_name = first_name,
        last_name = last_name
    )

    return user


@pytest.mark.django_db
def testUserPerson(person_form, create_same_person, create_person, firstNameLastName):

    assert person_form
    first_name, last_name = firstNameLastName
    assert first_name == "Algum"
    assert last_name == "Nome"
    assert create_same_person
    

#same_user, same_company = create_same_company

#user, company = create_company
