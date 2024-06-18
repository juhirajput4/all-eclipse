"""
Logging Demo 1
Logging Levels:-
DEBUG
INFO
WARNING8
ERROR
CRITICAL
"""


import logging
logging.basicConfig(filename="../Selenium Practice/testt.log", level=logging.WARNING)
#logging.warning("warning message")
logging.error("error message")
logging.info("info message")