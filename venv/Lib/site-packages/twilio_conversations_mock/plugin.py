import pytest

from client import ClientMock


@pytest.fixture
def Client():
    return ClientMock()
