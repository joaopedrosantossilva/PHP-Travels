import time
from telnetlib import EC

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.PageObject import PageObject


class HotelListPage(PageObject):

    #locators
    class_title = "sec__title_list"
    css_selector_5_star_hotel_title= "[data-star='5']"
    class_hoteis_elementos = "[class*='hotel_list']"
    id_check_5_stars = "stars_5"
    css_selector_morel_details = "a[class*='more_details']"

    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_city_name_in_title(self, city):
        print("title: "+self.driver.find_element(By.TAG_NAME, "title").text)
        return self.driver.title +city.upper()

    def get_number_of_5_star_hotels(self):
        hotels = self.driver.find_elements(By.CSS_SELECTOR, self.css_selector_5_star_hotel_title)
        return len(hotels)

    def get_number_of_hotels_listed(self):
        hotels = self.driver.find_elements(By.CLASS_NAME, self.class_hoteis_elementos)
        return len(hotels)

    def click_on_the_5_star_filter(self):
        self.driver.find_element(By.ID, self.id_check_5_stars).click()

    def the_number_of_5_star_hotels_is_equal_to_the_number_of_listed_hotels(self):
        return self.get_number_of_5_star_hotels() == self.get_number_of_hotels_listed()

    def filtrar_por_valores_de_preco(self):
        time.sleep(5)
        draggable = self.driver.find_element(By.CSS_SELECTOR, "form [class='irs-handle from']")
        ActionChains(self.driver).drag_and_drop_by_offset(draggable, 50, 0).perform()
        #ActionChains(self.driver).click_and_hold(draggable).move_by_offset(50, 50).perform()
        time.sleep(5)

    def clik_on_details_of_the_first_hotel_listed(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_selector_morel_details).click()






