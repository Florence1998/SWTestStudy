import logging
logging.basicConfig(filename='myapp.log',
                    level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s (%(filename)s:%(lineno)s)',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
logging.warning('is when this event was logged.')
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too')