import pytest

@pytest.fixture
def endpoint():
    return "/auth/google/redirect/"