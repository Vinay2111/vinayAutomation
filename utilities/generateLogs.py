import logging

#logging.basicConfig(filename="..\\logs\\logfile.log",format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.INFO)

#log = logging.getLogger()
#log.info("This is our first log")

'''now we are creating a function for generating logs'''

def log():
    logging.basicConfig(filename="..\\logs\\logfile.log", format='%(asctime)s: %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

    logger = logging.getLogger()
    return logger

logger=log()
logger.info("This is our first log")
logger.error("This is an error message") #to add error logs

