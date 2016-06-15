import logging
import mylib

logging.basicConfig(format='%(levelname)s:%(asctime)s:%(message)s', level=logging.INFO)
mylib.print_error()
logging.info("This is an info message in the main program")
logging.error("This is an error in the main program!")
