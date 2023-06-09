from pages.HotelBookingPage import HotelBookingPage
from pages.HotelInvoicePage import HotelInvoicePage
from pages.HotelsDetailsPage import HotelsDetailsPage
from pages.HotelsHomePage import HotelsHomePage
from pages.HotelsListPage import HotelListPage
from faker import Faker

class Test1:
    def test_find_hotel_in_dubai_for_one_adult(self, open_home, city='Dubai', city_country='Dubai United Arab Emirates'):
        qtd_adults = 1
        hotels_page = HotelsHomePage(driver=open_home.driver)
        hotels_page.click_on_hotels_tab()
        assert hotels_page.is_selected_hotel_tab(), "The hotel tab not selected"
        hotels_page.set_city_name(city)
        assert hotels_page.option_selected_in_the_city_name_field(city_country), "Value not informed in the city name field or different from the expected."
        hotels_page.set_number_of_adults(qtd_adults)
        assert hotels_page.is_quantity_total_adults(qtd_adults), "The number of adults is different than expected"
        hotels_page.search()
        hotels_list_page = HotelListPage(driver=hotels_page.driver)
        assert hotels_list_page.is_city_name_in_title(city), "The searched city was not displayed in the title of the page"

    def test_filter_for_a_5_star_dubai_hotel(self, open_home,city='Dubai', city_country='Dubai United Arab Emirates'):
        hotels_page = HotelsHomePage(driver=open_home.driver)
        hotels_page.click_on_hotels_tab()
        assert hotels_page.is_selected_hotel_tab(), "The hotel tab not selected"
        hotels_page.set_city_name(city)
        assert hotels_page.option_selected_in_the_city_name_field(city_country), "Value not informed in the city name field or different from the expected."
        hotels_page.search()
        hotels_list_page = HotelListPage(driver=hotels_page.driver)
        assert hotels_list_page.is_city_name_in_title(city), "The searched city was not displayed in the title of the page"
        hotels_list_page.click_on_the_5_star_filter()
        hotels_list_page.the_number_of_5_star_hotels_is_equal_to_the_number_of_listed_hotels(), "Number of 5 star hotels listed is different than correct"

    def test_filter_for_a_hotel_in_dubai_between_20_and_50(self, open_home, city='Dubai', city_country='Dubai United Arab Emirates'):
        hotels_page = HotelsHomePage(driver=open_home.driver)
        hotels_page.click_on_hotels_tab()
        assert hotels_page.is_selected_hotel_tab(), "The hotel tab not selected"
        hotels_page.set_city_name(city)
        assert hotels_page.option_selected_in_the_city_name_field(
            city_country), "Value not informed in the city name field or different from the expected."
        hotels_page.search()
        hotels_list_page = HotelListPage(driver=hotels_page.driver)
        assert hotels_list_page.is_city_name_in_title(city), "The searched city was not displayed in the title of the page"
        hotels_list_page.filtrar_por_valores_de_preco()

    def test_book_hotel_room_in_dubai_without_finalizing_payment(self, search_for_hotels_in_dubai):
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
        assert hotels_details.is_hotel_details_displayed(), 'No hotel details screen displayed'
        hotels_details.click_book_now_in_the_first_room()
        hotels_booking = HotelBookingPage(driver=hotels_details.driver)
        hotels_booking.set_your_personal_information(first_name_1,last_name_1,email,phone,address)
        hotels_booking.set_travellers_information(first_name_1,last_name_1,first_name_2,last_name_2)
        hotels_booking.click_in_by_continuing_you_agre_to_the_terms_and_conditions()
        hotels_booking.click_in_confirm_booking()
        hotels_invoice = HotelInvoicePage(driver=hotels_booking.driver)
        hotels_invoice.is_informacoes_pessoais_corretas()
