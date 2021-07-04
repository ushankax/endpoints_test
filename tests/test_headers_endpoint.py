from http import HTTPStatus

import requests
import pytest


@pytest.fixture()
def custom_headers():
    """
    Fixture with custom headers.
    """

    return {
        'content_type': {"Content-Type": "text/plain"},
        'some_headers_to_check': {
            "User-Agent": "ufo_hardware",
            "Content-Type": "application/json",
            "Accept-Language": "us",
            "Referer": "https://ozon.ru",
        }
    }


def test_headers_response_correct_status_code():
    """
    Check correct status code on headers GET-request.
    """

    headers_response = requests.get('https://httpbin.org/headers')

    result_status_code = headers_response.status_code

    assert result_status_code == HTTPStatus.OK


def test_headers_response_returns_headers_content():
    """
    Check GET-request headers from response exist.
    """

    headers_response = requests.get('https://httpbin.org/headers')
    assert headers_response.status_code == HTTPStatus.OK

    result_headers_content_length = len(headers_response.json().get('headers', None))

    assert result_headers_content_length > 0


def test_headers_response_correctly_returns_custom_headers(custom_headers):
    """
    Check that response correctly returns custom headers from fixture.
    """

    headers_response = requests.get('https://httpbin.org/headers', headers=custom_headers['some_headers_to_check'])
    assert headers_response.status_code == HTTPStatus.OK

    result_headers = headers_response.json().get('headers')

    assert result_headers.get('User-Agent') == 'ufo_hardware'
    assert result_headers.get('Content-Type') == 'application/json'
    assert result_headers.get('Accept-Language') == 'us'
    assert result_headers.get('Referer') == 'https://ozon.ru'


def test_headers_response_returns_correct_content_type(custom_headers):
    """
    Check that we get json content if send incorrect 'Content-Type'.
    """

    headers_response = requests.get('https://httpbin.org/headers', headers=custom_headers['content_type'])
    assert headers_response.status_code == HTTPStatus.OK

    result_content_type = headers_response.headers['Content-Type']

    assert result_content_type == 'application/json'
