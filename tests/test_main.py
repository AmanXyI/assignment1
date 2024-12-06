import time

import pytest
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from TestData.HomePageData import HomePageData
# from TestData import HomePageData
from pageObjects.CartPage import CartPage
from pageObjects.HomePage import HomePage
from utils.BaseClass import BaseClass


class TestMain(BaseClass):
    def test_main(self,getData):
        log=self.getLogger()
        self.driver.implicitly_wait(4)
        wait=WebDriverWait(self.driver,4)

        homepage=HomePage(self.driver)
        cartpage=CartPage(self.driver)

        homepage.getSignupBtn().click()
        homepage.getUserName().send_keys(getData["uname"])
        homepage.getPassword().send_keys(getData["upass"])
        homepage.getRegisterBtn().click()
        wait.until(expected_conditions.alert_is_present())
        signupAlert=self.driver.switch_to.alert
        signupAlert.accept()
        log.info("signup successful")
        homepage.getLoginBtn().click()
        homepage.getLoginUserName().send_keys(getData["uname"])
        homepage.getLoginPassword().send_keys(getData["upass"])
        homepage.getLoginRegisterBtn().click()
        log.info("login successful")

        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"Samsung galaxy s6")))
        time.sleep(3)
        productsList=homepage.getProduct()

        self.findProduct(productsList,"Samsung galaxy s6")
        homepage.getAddToCartBtn().click()
        wait.until(expected_conditions.alert_is_present())
        addedAlert=self.driver.switch_to.alert
        addedAlert.accept()

        homepage.getCartBtn().click()
        productText=cartpage.getProductName().text
        if productText == "Samsung galaxy s6":
            log.info("Product added to cart")
        else:
            log.error("Product not added to cart")
        cartpage.getPlaceOrder().click()
        cartpage.getName().send_keys(getData["details"])
        cartpage.getCountry().send_keys(getData["details"])
        cartpage.getCity().send_keys(getData["details"])
        cartpage.getCard().send_keys(getData["details"])
        cartpage.getMonth().send_keys(getData["details"])
        cartpage.getYear().send_keys(getData["details"])
        cartpage.getcontinuePurchase().click()
        successMsg=cartpage.getSuccessMsg().text
        if successMsg=="Thank you for your purchase!":
            log.info("order placed")
        else:
            log.error("order not placed")
        time.sleep(3)

    @pytest.fixture(params=HomePageData.test_homepagedata)
    def getData(self,request):
        return request.param

