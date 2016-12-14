#!/usr/bin/python

import logging

#create logger instance
logger = logging.getLogger('myfirstlogger')

#single config with the output and level of logging
#logger.basicConfig(filename='logger.log',level=logging.INFO)


logger.info('info message')
logger.error('error message')
logger.warn('warning message')
logger.critical('critical message')


