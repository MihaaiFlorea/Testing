from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class RadioCheckButtons():
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome('E:\\Program Files\\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get(self.url)

    def modalitate_plata(self, optiune_plata = 'cash'):
        if optiune_plata in ['cash', 'online', 'transfer']:
            optiune_plata = self.driver.find_element(By.XPATH, f"//input[@value = '{optiune_plata}']")
            try:
                optiune_plata.click()
            except:
                optiune_plata.click()
        else:
            print('Modalitate de plata invalida')

    def check_boxes(self):
        checkboxses = self.driver.find_elements(By.XPATH, "//div[@class = 'checkbox']//input[@type = 'checkbox']")
        for checkbox in checkboxses:
            if not checkbox.is_selected():
                try:
                    checkbox.click()
                except:
                    checkbox.click()
                time.sleep(3)
    def inregistrare(self):
        button = self.driver.find_element(By.XPATH, "//button[@class = 'btn btn-primary']")
        if button.is_enabled():
            button.click()
            time.sleep(3)
        else:
            print('Butonul de inregistrare nu este enabled')
    def stop(self):
        print(self.driver.current_url)
        self.driver.close()

inscriere = RadioCheckButtons('https://www.telacad.ro/modalitati-de-plata/')
time.sleep(2)
inscriere.modalitate_plata()
time.sleep(2)
# inscriere.modalitate_plata('online')
# time.sleep(3)
# inscriere.modalitate_plata('transfer')
# time.sleep(2)
inscriere.check_boxes()
inscriere.inregistrare()
inscriere.stop()
