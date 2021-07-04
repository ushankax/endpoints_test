from datetime import datetime
import logging
import os

import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call():
    try:
        outcome = yield
        outcome.get_result()
    except AssertionError:
        logging.exception('Caught AssertionError:')
        raise


def pytest_configure(config):
    """ Create a log file."""
    if not config.option.log_file:
        timestamp = datetime.strftime(datetime.now(), '%Y-%m-%d_%H-%M-%S')
        config.option.log_file = f'{os.path.dirname(os.path.realpath(__file__))}/logs/{timestamp}.log'
