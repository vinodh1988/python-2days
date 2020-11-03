import logging

logging.basicConfig(filename='mylog.log', filemode='a',format='%(asctime)s  %(process)d-%(levelname)s-%(message)s')

logging.warning('This message is a warning')
logging.error('serious error occured')