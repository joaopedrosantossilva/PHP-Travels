import time

from selenium.webdriver.common.by import By
from pages.PageObject import PageObject


class HotelInvoicePage(PageObject):

    #locators

    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_informacoes_pessoais_corretas(self):
        print(self.driver.find_element(By.XPATH, "//li[span='First Name:']").text)
        time.sleep(5)
