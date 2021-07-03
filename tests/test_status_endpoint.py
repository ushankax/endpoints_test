from http import HTTPStatus

import requests
import pytest


@pytest.mark.parametrize("http_status", list(HTTPStatus))
def test_status_post_request_returns_correct_response_status_code(http_status):
    """Check the status we sent in POST-request is equal to response status code."""
    assert requests.post(f'https://httpbin.org/status/{http_status}').status_code == http_status


@pytest.mark.parametrize("incorrect_http_status", [9, 99, 1000])
def test_status_post_request_with_incorrect_code_returns_502(incorrect_http_status):
    """Check incorrect status code in POST-request doesn't work and response is 502."""
    assert requests.post(f'https://httpbin.org/status/{incorrect_http_status}').status_code == HTTPStatus.BAD_GATEWAY


@pytest.mark.xfail(reason="possibly not good")
def test_status_post_request_with_incorrect_3_digit_code_returns_502():
    """Check non-existent 3-digit status doesn't work and returns 502."""
    assert requests.post('https://httpbin.org/status/999').status_code == HTTPStatus.BAD_GATEWAY


def test_status_post_request_with_text_status_code_returns_400():
    """Check string status code instead integer in POST-request doesn't work."""
    assert requests.post('https://httpbin.org/status/text_code').status_code == HTTPStatus.BAD_REQUEST


def test_status_post_request_with_empty_status_code_returns_404():
    """Check empty data in POST-request instead status code returns 404."""
    assert requests.post('https://httpbin.org/status/').status_code == HTTPStatus.NOT_FOUND


def test_status_post_request_with_two_status_codes_returns_one_of_them_in_response():
    """Check that several statuses in POST-request works correct."""
    assert requests.post('https://httpbin.org/status/200,300').status_code in (200, 300)


def test_status_post_request_with_two_codes_and_weights_returns_correct_response_status_code():
    """Check that POST-request with two status codes in format (code, weight) returns one of sent codes."""
    assert requests.post('https://httpbin.org/status/200:1,300:2').status_code in (200, 300)


def test_status_post_request_with_only_code_and_weight_returns_400():
    """Check that POST-request with only one status code in format (code, weight) doesn't work (400 code)."""
    assert requests.post('https://httpbin.org/status/200:1').status_code == HTTPStatus.BAD_REQUEST


def test_weight_in_status_post_request_works_correct():
    """Check code with more weight in POST-request returns more often."""
    code_count = {200: 0, 300: 0}
    for _ in range(10):
        status_code = requests.post('https://httpbin.org/status/200:10,300:1').status_code
        if status_code in (200, 300):
            code_count[status_code] += 1

    assert code_count[200] > code_count[300]
