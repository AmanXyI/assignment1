from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self,driver):
        self.driver=driver

    signupBtn=(By.XPATH,"//a[@id='signin2']")
    signupUsername=(By.ID,"sign-username")
    signupPassword=(By.ID,"sign-password")
    registerSignupBtn=(By.CSS_SELECTOR,"button[onclick='register()']")
    loginBtn=(By.XPATH,"//a[@id='login2']")
    loginUsername=(By.ID,"loginusername")
    loginPassword=(By.ID,"loginpassword")
    registerLoginBtn=(By.CSS_SELECTOR,"button[onclick='logIn()']")
    # verify login
    getproduct=(By.CSS_SELECTOR,"a[class='hrefch']")
    addtocartBtn=(By.CSS_SELECTOR,"a[class='btn btn-success btn-lg']")
    cartBtn=(By.ID,"cartur")


    def getSignupBtn(self):
        return self.driver.find_element(*HomePage.signupBtn)
    def getUserName(self):
        return self.driver.find_element(*HomePage.signupUsername)
    def getPassword(self):
        return self.driver.find_element(*HomePage.signupPassword)
    def getRegisterBtn(self):
        return self.driver.find_element(*HomePage.registerSignupBtn)
    def getLoginBtn(self):
        return self.driver.find_element(*HomePage.loginBtn)
    def getLoginUserName(self):
        return self.driver.find_element(*HomePage.loginUsername)
    def getLoginPassword(self):
        return self.driver.find_element(*HomePage.loginPassword)
    def getLoginRegisterBtn(self):
        return self.driver.find_element(*HomePage.registerLoginBtn)
    def getProduct(self):
        return self.driver.find_elements(*HomePage.getproduct)
    def getAddToCartBtn(self):
        return self.driver.find_element(*HomePage.addtocartBtn)


    def getCartBtn(self):
        return self.driver.find_element(*HomePage.cartBtn)


