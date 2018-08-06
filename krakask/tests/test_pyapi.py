import pytest

from mocket import Mocketizer
from mocket.mockhttp import Entry

from krakask.api import API, AsyncApi


@pytest.mark.trio
async def test_get_server_time():
    raise NotImplementedError





if __name__ == '__main__':
    pytest.main(['-s', __file__])