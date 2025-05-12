import pytest

@pytest.fixture
def endpoint(main_endpoint):
    return "/auth/google/redirect/"