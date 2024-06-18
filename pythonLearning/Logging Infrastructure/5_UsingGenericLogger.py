from Generic_Logger import GenericLogger
import logging

class UsingGenericLogger():
    """
    logger = GenericLogger(loggerName="classLogger", logLevel=logging.DEBUG)

    def method0(self):

        self.logger.warning("warning message")
        self.logger.info("info message")
        self.logger.error("error message")
        self.logger.debug("debug message")
        """

    def method1(self):
        mLogger = GenericLogger(loggerName="m1Logger", logLevel=logging.DEBUG, FMT='%(asctime)s: %(levelname)s: %(message)s')
        mLogger.warning("warning message")
        mLogger.info("info message")
        mLogger.error("error message")
        mLogger.debug("debug message")

    def method2(self):
        mLogger = GenericLogger(loggerName="m2Logger", logLevel=logging.INFO)
        mLogger.warning("warning message")
        mLogger.info("info message")
        mLogger.error("error message")
        mLogger.debug("debug message")


a = UsingGenericLogger()
a.method1()
a.method2()

