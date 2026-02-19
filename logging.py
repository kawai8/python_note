from logging import getLogger, Formatter, StreamHandler, FileHandler, DEBUG, INFO
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler, HTTPHandler
import sys

class Logging:
    def __init__(self, name=__name__, filename=None):
        self.logger = getLogger(name)
        self.logger.setLevel(DEBUG)


        if not self.logger.hasHandlers():

            # stream handler
            sh = StreamHandler(sys.stdout)
            sh.setLevel(INFO)
            sh_format = '%(levelname)-8s %(asctime)s %(message)s'
            sh_formatter = Formatter(sh_format)
            sh.setFormatter(sh_formatter)
            self.logger.addHandler(sh)

            # file handler
            if filename is not None:
                fh = RotatingFileHandler(filename, mode='a', maxBytes=1048576, backupCount=6)
                fh.setLevel(DEBUG)
                fh_format = '%(levelname)-8s %(asctime)s p=%(process)d %(message)s'
                fh_formatter = Formatter(fh_format)
                fh.setFormatter(fh_formatter)
                self.logger.addHandler(fh)
            else:
                print('No log file provided, please specify a log file.')
                sys.exit(9)


    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)
