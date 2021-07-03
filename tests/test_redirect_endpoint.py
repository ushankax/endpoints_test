from http import HTTPStatus

import requests


def test_get_request_request_makes_one_redirect_correctly():
    """Check 302 response status code when one redirect in GET-request."""
    assert requests.get('https://httpbin.org/redirect/1').status_code == HTTPStatus.FOUND


def test_get_request_request_redirects_more_than_one_times_correctly():
    """Check 302 response status code if we send in GET-request 2 redirects count."""
    assert requests.get('https://httpbin.org/redirect/2').status_code == HTTPStatus.FOUND


def test_get_request_request_doesnt_work_with_0_redirects():
    """Check that we get an error when send 0 redirects in GET-request."""
    assert requests.get('https://httpbin.org/redirect/0').status_code == HTTPStatus.NOT_FOUND


def test_get_request_request_doesnt_work_without_number_of_redirects():
    """Check that we get an error when don't send number of redirects in GET-request."""
    assert requests.get('https://httpbin.org/redirect/').status_code == HTTPStatus.NOT_FOUND
