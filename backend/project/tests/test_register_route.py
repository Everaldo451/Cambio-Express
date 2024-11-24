import pytest


@pytest.mark.django_db
def test_with_user_is_company(company_form, create_first_user, create_user,  create_company):

    user, userNotNone = create_user
    create_company, companyNotNone = create_company

    assert company_form
    assert userNotNone
    assert companyNotNone
