import json

import hypothesis.strategies
import pytest
import requests

from mocket import Mocketizer, Mocket
from mocket.mockhttp import Entry


@hypothesis.given(data=hypothesis.infer)
def test_connection_httpbin_get(data: int):
    url_to_mock = 'http://httpbin.org/get'

    Entry.single_register(
        Entry.GET,
        url_to_mock,
        body=json.dumps({"args": data}),
        headers={'content-type': 'application/json'}
    )

    with Mocketizer():
        session = requests.Session()
        resp = session.get(url_to_mock)
        assert "args" in resp.json() and resp.json()["args"] == data
        # ensure mocket actually replied to that
        assert len(Mocket._requests) == 1


@hypothesis.given(data=hypothesis.infer)
def test_connection_success(api, data: int):
    url_to_mock = api.get_url('Time', private=False)

    Entry.single_register(
        Entry.POST,
        url_to_mock,
        body=json.dumps({'data': data}),
        headers={'content-type': 'application/json'}
    )

    with Mocketizer():
        resp = api.query_public('Time')
        assert "args" in resp.json() and resp.json() == {'data': data}
        # ensure mocket actually replied to that
        assert len(Mocket._requests) == 1


if __name__ == '__main__':
    pytest.main(['-s', __file__])

