from ..src import connections
import pytest


# For integration tests:

@pytest.fixture
def redis():
    return connection.make_redis(host='test-server')
