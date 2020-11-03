import logging

logging.basicConfig(filename='mylog.log', filemode='w',format='%(asctime)s  %(process)d-%(levelname)s-%(message)s')

logging.warning('This message is a warning')
logging.error('serious error occured')