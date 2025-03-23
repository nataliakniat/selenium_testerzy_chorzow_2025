import pytest
import time
from selenium_testerzy_chorzow_2025.page_object_pattern.pages.search_hotel import SearchHotelPage
from selenium_testerzy_chorzow_2025.page_object_pattern.pages.serach_result import SearchResultPage
from selenium import webdriver

class TestHotelSearch:
    @pytest.fixture()  #czy na pewno ()
    def setup(self):
        # inicjalizacja przeglądarki Chrome
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        yield
        # zamkniecie przegladarki
        self.driver.quit()

    # test
    def test_hotel_search(self, setup):
        self.driver.get('http://www.kurs-selenium.pl/demo/')
        search_page = SearchHotelPage(self.driver)
        search_page.set_city("Dubai")
        search_page.set_date_range('23/03/2025','24/03/2025')
        search_page.set_travellers('1', '2')
        search_page.prerform_search()


