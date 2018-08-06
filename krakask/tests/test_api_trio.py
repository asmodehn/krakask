import json

import pytest

from mocket import Mocketizer
from mocket.mockhttp import Entry

from krakask.api import API, AsyncApi


class TrioApi(metaclass=AsyncApi):

    __asynclib__ = 'trio'

    async def sleep(self):
        import trio
        await trio.sleep(1)


@pytest.skipif()
@pytest.mark.trio
async def test_trio_sleep():

    api=TrioApi()
    await api.sleep()


@pytest.mark.trio
async def test_connection_error(api, mock_srv):
    with pytest.raises(ConnectionRefusedError):
        await api.query_public('Time')


import asks

@pytest.mark.trio
async def test_connection_httpbin(api):
    url_to_mock = 'http://httpbin.org/get'

    Entry.single_register(
        Entry.GET,
        url_to_mock,
        body=json.dumps({"args": {}}),
        headers={'content-type': 'application/json'}
    )

    with Mocketizer():
        session = asks.Session()
        resp = await session.get(url_to_mock,)

    assert "args" in resp.json() and resp["args"] == {}


@pytest.mark.trio
async def test_connection_success(api, mock_srv):
    url_to_mock = 'http://' + mock_srv + '/0/public/mocktest'

    Entry.single_register(
        Entry.GET,
        url_to_mock,
        body=json.dumps({'data': 42}),
        headers={'content-type': 'application/json'}
    )

    #responses.add(responses.GET, 'https://' + mock_srv + '/0/public/mocktest',
    #              json={'data': 42}, status=404)

    with Mocketizer():
        resp = await api.query_public('mocktest')

    assert resp.json() == {'data': 42}

    #assert len(responses.calls) == 1
    #assert responses.calls[0].request.url == 'https://' + mock_srv + '/0/public/mocktest'
    #assert responses.calls[0].response.text == '{"data": 42}'








if __name__ == '__main__':
    pytest.main(['-s', __file__])

