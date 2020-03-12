# Python 3.6.5

import logging

class testLogging(object):
    def __init__(self):
        logger = logging.getLogger()

        logFormat = logging.Formatter('%(asctime)-18s : %(name)-10s - %(levelname)-8s - %(message)-12s')
        logFileName = "04_Loggging.txt"

        fh = logging.FileHandler(logFileName)
        fh.setLevel(logging.INFO)
        fh.setFormatter(logFormat)
        logger.addHandler(fh)
        
        # logging.basicConfig(level = logging.INFO, format = logFormat, filename = logFileName, filemode = "w")
        logging.debug("debug message")
        logging.info("info message")
        logging.warning("warning message")
        logging.error("error message")
        logging.critical("critical message")

if __name__ == "__main__":
    t = testLogging()