import time

from selenium.webdriver.common.by import By

from pages.PageObject import PageObject

class HomePage(PageObject):
    # Locators
    url = 'https://phptravels.net/'


    def __init__(self, browser):
        super().__init__(browser=browser)
        self.open_home_page()

    def open_home_page(self):
        self.driver.get(self.url)

    def select_the_language_english(self):
        self.driver.find_element(By.ID, 'languages').click()
        self.driver.find_element(By.CSS_SELECTOR, "[href='https://phptravels.net/lang-en']").click()
        time.sleep(5)









