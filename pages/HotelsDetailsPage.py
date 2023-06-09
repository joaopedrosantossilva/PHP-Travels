import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.PageObject import PageObject


class HotelsDetailsPage(PageObject):

    #locators

    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_hotel_details_displayed(self):
        element = '[data-scroll=description]'
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, element)))
        return self.driver.find_element(By.CSS_SELECTOR, element).text == 'Hotel Details'

    def clicar_em_hotels_details(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-scroll=description]').click()

    def click_book_now_in_the_first_room(self):
        self.clicar_em_hotels_details()
        element = '.card-body button'
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, element).click()
        time.sleep(5)




