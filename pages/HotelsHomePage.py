import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.PageObject import PageObject
from selenium.webdriver.common.keys import Keys

class HotelsHomePage(PageObject):
    # locators
    id_hotels_tab = "hotels-tab"
    css_selector_city_name_select = "[aria-labelledby='select2-hotels_city-container']"
    css_selector_first_option_list_In_city_name = '#select2-hotels_city-results li'
    css_selector_travellers_select = "#hotels-search .col-md-3 a"
    css_selector_adults_input = '#hotels_adults.qtyInput_hotels'
    css_selector_hotel_tab_selecionada = "[data-bs-target='#tab-hotels'][aria-selected='true']"
    id_buscar_button = "[id='hotels-search'] button"
    css_selector_diminuir_qtd_adultos = "#hotels-search [class='dropdown-menu dropdown-menu-wrap'] .dropdown-item:nth-child(2) .qtyDec"
    css_selector_aumentar_qtd_adultos = "#hotels-search [class='dropdown-menu dropdown-menu-wrap'] .dropdown-item:nth-child(2) .qtyInc"
    css_selector_city_input = "[aria-controls='select2-hotels_city-results']"
    class_qtd_hotel_span = "guest_hotels"
    class_lista_cidades_sugeridas = "[class='most--popular-hotels'] strong"
    id_valor_selecionado_no_campo_city_name = "select2-hotels_city-container"

    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_selected_hotel_tab(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.css_selector_hotel_tab_selecionada).is_displayed()

    def click_on_hotels_tab(self):
        self.driver.find_element(By.CSS_SELECTOR, "[data-bs-target='#tab-hotels']").click()

    def set_city_name(self, city):
        self.driver.find_element(By.CSS_SELECTOR, self.css_selector_city_name_select).click()
        self.driver.find_element(By.CSS_SELECTOR, self.css_selector_city_input).send_keys(city)
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, self.css_selector_city_input).send_keys(Keys.ENTER)

    def set_number_of_adults(self, new_qtd):
        self.driver.find_element(By.CSS_SELECTOR, self.css_selector_travellers_select).click()
        qtd_atual = int(self.driver.find_element(By.CSS_SELECTOR, self.css_selector_adults_input).get_attribute("value"))
        if qtd_atual > new_qtd:
            diminuir = qtd_atual - new_qtd
            for i in range(diminuir):
                self.driver.find_element(By.CSS_SELECTOR, self.css_selector_diminuir_qtd_adultos).click()
        elif qtd_atual < new_qtd:
            aumentar = new_qtd - qtd_atual
            for i in range(aumentar):
                self.driver.find_element(By.CSS_SELECTOR, self.css_selector_aumentar_qtd_adultos).click()

    def search(self):
        self.driver.find_element(By.CSS_SELECTOR, self.id_buscar_button).click()

    def is_quantity_total_adults(self, qtd):
        return self.driver.find_element(By.CLASS_NAME, self.class_qtd_hotel_span).text == str(qtd)

    def wait_and_verify_the_first_option_in_the_list_of_cities(self, suggested_city):
        element = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.class_lista_cidades_sugeridas)))
        print(element.text)
        return element.text == suggested_city

    def click_on_the_first_suggested_citty_option_in_the_list(self):
        self.driver.find_element(By.CSS_SELECTOR, self.class_lista_cidades_sugeridas).click()

    def option_selected_in_the_city_name_field(self, city):
        return self.driver.find_element(By.ID, self.id_valor_selecionado_no_campo_city_name).text == city

