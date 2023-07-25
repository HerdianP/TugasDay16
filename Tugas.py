
import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        service = ChromeService(executable_path="\TugasDay16\TugasDay16\chromedriver.exe")
        self.browser = webdriver.Chrome(service=service, options=options)
    def test_a_success_login(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.CLASS_NAME,"title").text
        self.assertIn('Products', response_data)

    def test_b_check_click_product(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "inventory_item_name").click()
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.ID,"back-to-products").text
        self.assertIn('Back to products', response_data)

    def test_c_success_checkout(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "shopping_cart_badge").click()
        time.sleep(1)
        driver.find_element(By.ID, "checkout").click()
        time.sleep(1)
        driver.find_element(By.ID, "first-name").send_keys("Sanber")
        time.sleep(1)
        driver.find_element(By.ID, "last-name").send_keys("Code")
        time.sleep(1)
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        time.sleep(1)
        driver.find_element(By.ID, "continue").click()
        time.sleep(1)
        driver.find_element(By.ID, "finish").click()
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.CLASS_NAME,"title").text
        self.assertIn('Checkout: Complete!', response_data)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()