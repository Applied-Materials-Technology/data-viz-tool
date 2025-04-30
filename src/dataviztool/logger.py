import logging
import sys


logger = logging.getLogger(__name__)
#logging.basicConfig(level=logging.INFO)

stdout = logging.StreamHandler(stream=sys.stdout)

fmt = logging.Formatter("%(name)s: %(asctime)s | %(levelname)s | %(filename)s:%(lineno)s | %(process)d >>> %(message)s")

stdout.setFormatter(fmt)

#stdout.setLevel(logging.INFO)

logger.addHandler(stdout)
logger.setLevel(logging.INFO)

logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
