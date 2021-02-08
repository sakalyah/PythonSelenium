#import logging

#logging.warning("This is a Warning Message")
#logging.info("This is INformation")
#logging.debug("Used While Debugging")
#logging.error("Error Message")
#logging.critical("Critical Error")

#logging.basicConfig(filename="logdemo.log",level=logging.DEBUG)
'''
logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s",level=logging.INFO)
logging.warning("This is a Warning Message")
logging.info("This is INformation")
logging.debug("Used While Debugging")
logging.error("Error Message")
logging.critical("Critical Error")
'''
import logging
class loggind_demo():

    def test(self):
        #CReate Logger
        logger = logging.getLogger('Harish')
        #Set Level
        logger.setLevel(logging.WARNING)
        #Create Console Handler and Set Level Info
        c_handler = logging.StreamHandler()
        c_handler.setLevel(logging.INFO)

        #Create Formatter
        format = logging.Formatter('%(asctime)s %(levelname)s %(message)s %(levelno)s')
        c_handler.setFormatter(format)

        #Add Console Handler to Logger
        logger.addHandler(c_handler)

        logger.warning("This is a Warning Message")
        logger.info("This is INformation")
        logger.debug("Used While Debugging")
        logger.error("Error Message")
        logger.critical("Critical Error")


D = loggind_demo()
D.test()