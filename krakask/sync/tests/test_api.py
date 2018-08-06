import json

import hypothesis.strategies
import pytest
import requests

from mocket import Mocketizer
from mocket.mockhttp import Entry


def test_connection_error(api, mock_srv):
    with pytest.raises(requests.exceptions.ConnectionError):
        api.query_public('Time')


@hypothesis.given(data=hypothesis.infer)
def test_connection_httpbin(data: int):
    url_to_mock = 'http://httpbin.org/get'

    Entry.single_register(
        Entry.GET,
        url_to_mock,
        body=json.dumps({"args": data}),
        headers={'content-type': 'application/json'}
    )

    with Mocketizer():
        session = requests.Session()
        resp = session.get(url_to_mock,)

    assert "args" in resp.json() and resp.json()["args"] == data


@hypothesis.given(data=hypothesis.infer)
def test_connection_success(api, mock_srv, data: int):
    url_to_mock = 'https://' + mock_srv + '/0/public/Time'

    Entry.single_register(
        Entry.GET,
        url_to_mock,
        body=json.dumps({'data': data}),
        headers={'content-type': 'application/json'}
    )

    #responses.add(responses.GET, 'https://' + mock_srv + '/0/public/mocktest',
    #              json={'data': 42}, status=404)

    with Mocketizer():
        resp = api.query_public('Time')

    assert "args" in resp.json() and resp.json() == {'data': data}

    #assert len(responses.calls) == 1
    #assert responses.calls[0].request.url == 'https://' + mock_srv + '/0/public/mocktest'
    #assert responses.calls[0].response.text == '{"data": 42}'



if __name__ == '__main__':
    pytest.main(['-s', __file__])

