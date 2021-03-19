import logging

#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')

#logging.debug('This is a debug message')
#logging.info('This is an info message')
#logging.warning('This is a warning message')
#logging.error('This is an error message')
#logging.critical('This is a critical message')

#import helper

#logger = logging.getLogger(__name__)

###### create handler
#stream_h = logging.StreamHandler()
#file_h = logging.FileHandler('file.log')

###### level and the format
#stream_h.setLevel(logging.WARNING)
#file_h.setLevel(logging.ERROR)

#formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
#stream_h.setFormatter(formatter)
#file_h.setFormatter(formatter)

#logger.addHandler(stream_h)
#logger.addHandler(file_h)

#logger.warning('this is a warning')
#logger.error('this is an error')

import traceback

try:
    a = [1, 2, 3]
    val = a[4]
except IndexError as e:
    logging.error("The error is %s", traceback.format_exc())