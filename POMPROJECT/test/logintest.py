from Scripts.POMPROJECT.pages.login import loginpage
#from scripts.POMproject.pages.login import homepage
from selenium import webdriver
import time
import unittest

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(2000)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://orangehrm-demo-6x.orangehrmlive.com/auth/login")
        login = loginpage(driver)
        login.enter_username("admin")
        login.enter_pwd("admin123")
        login.enter_btn()
        driver.implicitly_wait(2000)
        #homepage = homepage(driver)
        #homepage.click_welcome()
        #driver.implicitly_wait(2000)
        #homepage.click_logout()

    @classmethod
    def teardownclass(cls):
        cls.time.sleep(2000)
        cls.driver.close()
        cls.driver.quit()
        print("test completed")

if __name__ == '__main__':
    unittest.main()

