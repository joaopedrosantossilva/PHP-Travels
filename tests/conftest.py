import pytest
from faker import Faker

from pages.HotelBookingPage import HotelBookingPage
from pages.HotelInvoicePage import HotelInvoicePage
from pages.HotelsDetailsPage import HotelsDetailsPage
from pages.HotelsHomePage import HotelsHomePage
from pages.HotelsListPage import HotelListPage
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage

def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Set browser")

@pytest.fixture()
def choose_browser(request):
    selected_browser = request.config.getoption("--browser").lower()
    yield selected_browser

@pytest.fixture()
def open_login(choose_browser):
    login_page = LoginPage(browser=choose_browser)
    yield login_page
    login_page.close()

@pytest.fixture()
def efetuar_login(open_login):
    print("efetuar login")
    open_login.efetuar_login()
    yield open_login

@pytest.fixture()
def open_home(choose_browser):
    home_page = HomePage(browser=choose_browser)
    yield home_page

@pytest.fixture()
def search_for_hotels_in_dubai(open_home):
    hotels_page = HotelsHomePage(driver=open_home.driver)
    hotels_page.set_city_name('Dubai')
    hotels_page.search()
    hotels_list_page = HotelListPage(driver=hotels_page.driver)
    yield hotels_list_page

@pytest.fixture()
def hotel_reservation_in_dubai_pending_payment(search_for_hotels_in_dubai):
    generator = Faker()
    #Guest 1
    first_name_1 = generator.unique.first_name()
    last_name_1 = generator.unique.last_name()
    email = first_name_1+'@teste.com'
    phone = generator.msisdn()
    address = generator.address()
    #Guest 2
    first_name_2 = generator.unique.first_name()
    last_name_2 = generator.unique.last_name()
    hotels_list_page = HotelListPage(driver=search_for_hotels_in_dubai.driver)
    hotels_list_page.clik_on_details_of_the_first_hotel_listed()
    hotels_details = HotelsDetailsPage(driver=hotels_list_page.driver)
    hotels_details.click_book_now_in_the_first_room()
    hotels_booking = HotelBookingPage(driver=hotels_details.driver)
    hotels_booking.set_your_personal_information(first_name_1, last_name_1, email, phone, address)
    hotels_booking.set_travellers_information(first_name_1, last_name_1, first_name_2, last_name_2)
    hotels_booking.click_in_by_continuing_you_agre_to_the_terms_and_conditions()
    hotels_booking.click_in_confirm_booking()
    hotels_invoice = HotelInvoicePage(driver=hotels_booking.driver)
    yield hotels_invoice

