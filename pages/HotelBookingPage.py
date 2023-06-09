import time

from faker import Faker
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.PageObject import PageObject


class HotelBookingPage(PageObject):

    #locators
    id_agree_checkbox = 'agreechb'
    id_booking_button = 'booking'
    name_first_name_in_your_personal_information_input = 'firstname'
    name_last_name_in_your_personal_information_input = 'lastname'
    name_email_in_your_personal_information_input = 'email'
    name_address_in_your_personal_information_input = 'address'
    name_phone_in_your_personal_information_input = 'address'
    name_first_name_traveller_1_in_travellers_information_input = 'firstname_1'
    name_last_name_traveller_1_in_travellers_information_input = 'lastname_1'
    name_first_name_traveller_2_in_travellers_information_input = 'firstname_2'
    name_last_name_traveller_2_in_travellers_information_input = 'lastname_2'

    def __init__(self, driver):
        super().__init__(driver=driver)

    def set_your_first_name_in_your_personal_information(self, first_name):
        self.driver.find_element(By.NAME, self.name_first_name_in_your_personal_information_input).send_keys(first_name)

    def set_your_last_name_in_your_personal_information(self, last_name):
        self.driver.find_element(By.NAME, self.name_last_name_in_your_personal_information_input).send_keys(last_name)

    def set_your_email_in_your_personal_information(self, email):
        self.driver.find_element(By.NAME, self.name_email_in_your_personal_information_input).send_keys(email)

    def set_your_phone_in_your_personal_information(self, phone):
        self.driver.find_element(By.NAME, self.name_phone_in_your_personal_information_input).send_keys(phone)

    def set_your_address_in_your_personal_information(self, address):
        self.driver.find_element(By.NAME, self.name_address_in_your_personal_information_input).send_keys(address)

    def set_first_name_traveller_1_in_travellers_information(self, first_name):
        self.driver.find_element(By.NAME, self.name_first_name_traveller_1_in_travellers_information_input).send_keys(first_name)

    def set_last_name_traveller_1_in_travellers_information(self, last_name):
        self.driver.find_element(By.NAME,  self.name_last_name_traveller_1_in_travellers_information_input).send_keys(last_name)

    def set_first_name_traveller_2_in_travellers_information(self, first_name):
        self.driver.find_element(By.NAME,  self.name_first_name_traveller_2_in_travellers_information_input).send_keys(first_name)

    def set_last_name_traveller_2_in_travellers_information(self, last_name):
        self.driver.find_element(By.NAME, self.name_last_name_traveller_2_in_travellers_information_input).send_keys(last_name)

    def set_your_personal_information(self, first_name, last_name, email, phone, address):
        self.set_your_first_name_in_your_personal_information(first_name)
        self.set_your_last_name_in_your_personal_information(last_name)
        self.set_your_email_in_your_personal_information(email)
        self.set_your_phone_in_your_personal_information(phone)
        self.set_your_address_in_your_personal_information(address)

    def set_travellers_information(self,first_name_1, last_name_1,first_name_2,last_name_2):
        self.set_first_name_traveller_1_in_travellers_information(first_name_1)
        self.set_last_name_traveller_1_in_travellers_information(last_name_1)
        self.set_first_name_traveller_2_in_travellers_information(first_name_2)
        self.set_last_name_traveller_2_in_travellers_information(last_name_2)

    def click_in_by_continuing_you_agre_to_the_terms_and_conditions(self):
        self.driver.execute_script("document.getElementById('"+self.id_agree_checkbox+"').click();")

    def click_in_confirm_booking(self):
        time.sleep(5)
        self.driver.find_element(By.ID, self.id_booking_button).click()








