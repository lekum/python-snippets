import logging

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

def print_error():
    log.error("This is an error generated in the library!")

