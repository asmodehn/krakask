
from ..api import API
from ..pyapi import KrakenAPI, KrakenAPIError

import pytest
import hypothesis


@pytest.fixture
def mocket(mock_srv):
    """
    fixture generating data based on hypothesis strategies
    :param mocket:
    :return:
    """

    api = API()
    # to make sure we can never actually reach out
    api.uri = 'http://' + mock_srv
    return api


@pytest.fixture
def api():
    api = API()
    return api


@pytest.fixture
def pyapi(api):
    return KrakenAPI(api)

