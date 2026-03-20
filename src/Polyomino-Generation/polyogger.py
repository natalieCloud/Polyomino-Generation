import logging

logger = None

def get_logger():
    global logger
    
    if logger:
        return logger
    else:
        logger = logging.getLogger("polyomino")
        logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
        return logger
