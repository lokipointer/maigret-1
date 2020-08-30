import pytest

def pytest_addoption(parser):
    parser.addoption('--site', action='store', help='site name')


@pytest.fixture(scope='session')
def site(request):
    return request.config.option.site

