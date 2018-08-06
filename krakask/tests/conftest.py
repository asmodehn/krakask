
#from krakask.api import API
#from krakask.pyapi import KrakenAPI, KrakenAPIError

import pytest


@pytest.fixture
def mock_srv():
    return "127.0.0.1"


# @pytest.fixture
# def api(mock_srv):
#     """A flaky webserver with pathological behavior for testing purposes"""
#     api = API()
#     # to make sure we can never actually reach out
#     api.uri = 'http://' + mock_srv
#     return api
#
#
# @pytest.fixture
# def pyapi(api):
#     return KrakenAPI(api)

