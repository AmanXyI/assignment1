import inspect

import pytest
import logging


@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self):
        loggerName=inspect.stack()[1][3]
        logger=logging.getLogger(loggerName)

        fileHandler=logging.FileHandler('logfile.log')

        formatter=logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")

        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger
    def verifyLinkPresence(self,text):
        pass
    def findProduct(self,locator,productName):
        list=locator
        for product in list:
            print(product)
            if product.text ==productName:
                product.click()
                return

