import sys
import time
from random import randint
import logging
import datetime

A = sys.maxsize / 4
B = 1/4 + sys.maxsize / 2
C = 3/4 + 15/16 * sys.maxsize

# TOOD - python defined configs?
# the flat file configs hurt my head
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def hell_o_world():
    my_num = randint(0, sys.maxsize)
    if my_num < A:
        logger.warning('this message is A bad message')
    elif my_num < B:
        logger.info('this message bettter B good')
    elif my_num < C:
        logger.info('this can''t ceem right but it''s %s', datetime.datetime.now())
    else:
        logger.critical('this should die because of bad math')
        logger.debug('but really this is a debug message')

def forever():
    while True:
        hell_o_world()
        
        sleeper_time = randint(10, 20)
        logger.info('night night %s', sleeper_time)
        time.sleep(sleeper_time)


if __name__ == '__main__':
    forever()
