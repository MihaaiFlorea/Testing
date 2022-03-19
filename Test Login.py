from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
import unittest
import time

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s <%(levelname)s> - %(funcName)s : %(message)s',
                    datefmt='%H %M')

class TestLogin(unittest.TestCase):
    URL = 'https://cursuri.telacad.ro/'
    email = 'mihaaiflorea@gmail.com'
    password = 'Test147'

    def setUp(self):
        logging.info(f"Start sesion with: {self.URL}")
        self.driver = webdriver.Chrome('E:\\Program Files\\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get(self.URL)
        time.sleep(2)
        self.button_login = self.driver.find_element(By.XPATH, "//div[@class = 'mobile-nav-item hidden-mobile nav-item']//a[@class='sign-in-btn btn']")
        self.button_login.click()
        time.sleep(3)
        self.box_email = self.driver.find_element(By.ID, 'login-email')
        self.box_password = self.driver.find_element(By.ID, 'login-password')
        self.button_conect = self.driver.find_element(By.XPATH, "//button[@type = 'submit']")

    def test_aut(self):
        self.box_email.send_keys(self.email)
        self.box_password.send_keys(self.password)
        self.button_conect.click()
        time.sleep(2)
        title_page = self.driver.find_element(By.XPATH, "//*[@class = 'header-courses']").get_attribute('innerText')
        self.assertIn('Cursurile mele', title_page, 'Error login')
        logging.info('Correct login')

    def test_aut_fail(self):
        self.box_email.send_keys('error@email.com')
        self.box_password.send_keys('errorlogin147')
        self.button_conect.click()
        time.sleep(2)
        error_message = self.driver.find_element(By.XPATH, "//*[@class ='message-title']").get_attribute('innerText')
        self.assertIn('Nu v-am putut conecta.', error_message, 'Error fail login')
        logging.info('Fail login successful')

    def tearDown(self):
        logging.info(f'Stop session with {self.driver.current_url}')
        self.driver.quit()
