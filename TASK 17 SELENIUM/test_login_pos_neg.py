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
        
    def test_Login_Negatif_1(self): 
        driver = self.driver
        driver.get("https://www.saucedemo.com/") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("abc") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()

        response_message = driver.find_element(By.ID,"spanMessage").text
        self.assertEqual(response_message, 'Epic sadface: Username and password do not match any user in this service')

    def test_Login_Positif(self): 
        driver = self.driver
        driver.get("https://www.saucedemo.com/") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("standard_user") # isi username
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()

unittest.main()