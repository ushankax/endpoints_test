from datetime import datetime
import logging
import os

log = logging.getLogger(__name__)


def pytest_assertrepr_compare(op, left, right):
    """This function will print log everytime when assert fails."""
    log.error(f'AssertionError: {left} {op} {right} \n')
    return ["AssertionError:", f'{left} {op} {right}']


def pytest_exception_interact(node, call, report):
    """Additional info for logs."""
    log.error(f'{node}')
    log.error(f'{report}')


def pytest_configure(config):
    """ Create a log file."""
    if not config.option.log_file:
        timestamp = datetime.strftime(datetime.now(), '%Y-%m-%d_%H-%M-%S')
        config.option.log_file = f'{os.path.dirname(os.path.realpath(__file__))}/logs/{timestamp}.log'
