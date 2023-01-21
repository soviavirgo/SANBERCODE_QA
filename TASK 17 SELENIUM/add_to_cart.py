import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginRegister(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_addtocart(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("standard_user") # isi username
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()
        time.sleep(1)
        driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR,".shopping_cart_link").click()
        time.sleep(3)
        driver.find_element(By.ID, "continue-shopping").click()
        time.sleep(5)

unittest.main()