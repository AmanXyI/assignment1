from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self,driver):
        self.driver=driver

    placeorderBtn=(By.XPATH,"//button[normalize-space()='Place Order']")
    productName=(By.CSS_SELECTOR,"td:nth-child(2)")
    name=(By.ID,"name")
    country=(By.ID,"country")
    city=(By.ID,"city")
    card=(By.ID,"card")
    month=(By.ID,"month")
    year=(By.ID,"year")
    successMsg=(By.XPATH,"//h2[normalize-space()='Thank you for your purchase!']")
    continuePurchase=(By.CSS_SELECTOR,"button[onclick='purchaseOrder()']")

    def getPlaceOrder(self):
        return self.driver.find_element(*CartPage.placeorderBtn)
    def getProductName(self):
        return self.driver.find_element(*CartPage.productName)
    def getName(self):
        return self.driver.find_element(*CartPage.name)
    def getCountry(self):
        return self.driver.find_element(*CartPage.country)
    def getCity(self):
        return self.driver.find_element(*CartPage.city)
    def getCard(self):
        return self.driver.find_element(*CartPage.card)
    def getMonth(self):
        return self.driver.find_element(*CartPage.month)
    def getYear(self):
        return self.driver.find_element(*CartPage.year)
    def getSuccessMsg(self):
        return self.driver.find_element(*CartPage.successMsg)
    def getcontinuePurchase(self):
        return self.driver.find_element(*CartPage.continuePurchase)
