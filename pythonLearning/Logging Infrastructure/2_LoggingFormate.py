import logging
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%y %I:%M:%S:%p', filename='../Selenium Practice/abc.log', level=logging.DEBUG)
logging.warning("warning message")
logging.info("info message")
logging.error("error message")