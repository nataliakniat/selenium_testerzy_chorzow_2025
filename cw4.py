tests\test_hotel_search.py: 18(TestHotelSearch.test_hotel_search)
self = < test_hotel_search.TestHotelSearch
object
at
0x000001D758B71D10 >
setup = None


def test_hotel_search(self, setup):
    self.driver.get("http://www.kurs-selenium.pl/")
    search_hotel_page = SearchHotelPage(self.driver)
    search_hotel_page.set_city("Dubai")
    search_hotel_page.set_date_range("14/02/2024", "17/02/2024")
    search_hotel_page.set_travellers("3", "1")
    search_hotel_page.perform_search()

    # druga czesc
    results_page = SearchResultsPage(self.driver)
    hotel_names = results_page.get_hotel_names()
    hotel_prices = results_page.get_hotel_prices()

    print(hotel_names)

> assert hotel_names[0] == "Jumeirah Beach Hotel"
E
TypeError: 'NoneType'
object is not subscriptable

test_hotel_search.py: 34: TypeError

Process
finished
with exit code 1
