import logging

class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver
        self.hotel_names_xpath = "//h4[contains(@class, 'list_title')]//b"
        self.hotel_prices_xpath = "//div[contains(@class, 'price_tab')]//b"


    def get_hotel_names(self):
        hotels = self.driver.find_elements("xpath", self.hotel_names_xpath)
        names = [hotel.get_attribute("textContent") for hotel in hotels]
        return names

    def get_hotel_prices(self):
        prices = self.driver.find_elements("xpath", self.hotel_prices_xpath)
        prices = [price.get_attribute('textContent') for price in prices]
        return prices

