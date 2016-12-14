#!/usr/bin/python

import logging
import logging.config


logging.config.fileConfig("./logging.conf")


def config_logger_with_file():
    # setup logger
    my_first_logger = logging.getLogger('myfirstlogger')
    # create file handler
    # printf log info
    my_first_logger.debug('debug message')
    my_first_logger.info('info message')
    my_first_logger.error('error message')
    my_first_logger.warn('warning message')
    my_first_logger.critical('critical message')

# create logger instance by manual configuration


def manual_config_logger():
    # setup logger
    my_first_logger = logging.getLogger('myfirstlogger')
    my_first_logger.setLevel(logging.DEBUG)
    # create file handler
    log_path = "./manual_log.log"
    my_first_handler = logging.FileHandler(log_path, 'a')
    my_first_handler.setLevel(logging.DEBUG)
    # create formatter
    fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d\
        %(process)d %(message)s"
    date_fmt = "%a %d %b %Y %H:%M:%S"
    formatter = logging.Formatter(fmt, date_fmt)
    # add handler and formatter to my_first_logger
    my_first_handler.setFormatter(formatter)
    my_first_logger.addHandler(my_first_handler)
    # printf log info
    my_first_logger.debug('debug message')
    my_first_logger.info('info message')
    my_first_logger.error('error message')
    my_first_logger.warn('warning message')
    my_first_logger.critical('critical message')

    # single config with the output and level of logging


def main():
    # Create classes by default using the system
    # logging.basicConfig(filename='logger.log',level=logging.DEBUG)
    # logging.info('info message')
    # logging.error('error')
    # logging.warn('warning message')
    # logging.critical('critical message')
    # manual_config_logger()
    # config_logger_with_file()
    # use the configfile to create logger
    logger = logging.getLogger("example01")
    logger.info("info message")

if __name__ == "__main__":
    main()
