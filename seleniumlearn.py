import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
#from page input locator 
from data import datanya

class TestLoginRegister(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_Login_Negatif_1(self): 
        driver = self.driver
        driver.get("https://www.saucedemo.com/") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("datanya.namasalah") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("datanya.passwordsalah") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()

        response_message = driver.find_element(By.ID,"spanMessage").text
        self.assertEqual(response_message, 'Invalid credentials')

    def test_Login_Positif(self): 
        driver = self.driver
        driver.get("https://www.saucedemo.com/") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("datanya.namabenar") # isi username
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("datanya.passwordbenar") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()


    def test_Job(self):
        driver = self.driver
        driver.get("hhttps://www.saucedemo.com/") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"menu_admin_viewAdminModule").click()
        driver.find_element(By.ID,"menu_admin_Job").click()
        driver.find_element(By.ID,"menu_admin_viewJobTitleList").click()
        time.sleep(3)
        driver.find_element(By.ID,"btnAdd").click()
        time.sleep(3)
        driver.find_element(By.ID,"jobTitle_jobTitle").send_keys("jobjobjobjob")

unittest.main()