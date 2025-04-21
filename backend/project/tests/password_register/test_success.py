from authe.form import RegisterForm, CompanyRegisterExtras, UserRegisterExtras
from django.db import transaction, IntegrityError
from api.models import Company
import pytest

@pytest.mark.django_db
def test_user_company(company_form, create_same_company, verify_user, create_company, user_data):

    assert company_form
    assert verify_user is None
    assert create_company is not None
    user, company = create_company
    assert company.CNPJ == user_data.get("CNPJ")
    assert company.name == user_data.get("name")