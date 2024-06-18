import logging
#https://docs.python.org/3/library/time.html
class LoggerConsole():
    def testLog(self):

        # Create logger
        logger = logging.getLogger('sample_logger')
        logger.setLevel(logging.INFO)

        # create console (StreamHandler()) handler which will help in printing on console
        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(logging.INFO)

        # Create formatter
        formatter = logging.Formatter('%(asctime)s: %(name)s: %(levelname)s: %(message)s', datefmt='%m/%d/%y %I:%M:%S:%p')

        # Add formatter to console handler
        consoleHandler.setFormatter(formatter)

        # Add console handler to logger
        logger.addHandler(consoleHandler)

        logger.warning("warning message")
        logger.info("info message")
        logger.error("error message")
        logger.debug("debug message")

a = LoggerConsole()
a.testLog()