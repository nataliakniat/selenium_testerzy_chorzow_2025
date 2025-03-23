import pytest
import time
from selenium_testerzy_chorzow_2025.page_object_pattern.pages.google_search import SearchPage
from selenium_testerzy_chorzow_2025.page_object_pattern.pages.google_result import ResultPage
from selenium import webdriver

@pytest.fixture
def driver():
    # inicjalizacja przeglądarki Chrome
    driver = webdriver.Chrome()
    yield driver
    # zamkniecie przegladarki
    driver.quit()

# test
def test_google_serach(driver):
    # stworzenie obiektu klasy Search Page
    search_page = SearchPage(driver)
    search_page.open()

    #sprawdzenie czy tytuł zakładki jest zgodny z oczekiwanym
    assert "Google" in driver.title

    # lokalizacja przycisku, zeby zaakceptowac zgody
    search_page.accept_cookies()

    # wprawadzenie hasla do wyszukania i szukanie
    search_page.search("Najlepsza kawa w Polsce")

    time.sleep(20)

    #Stworzenie obiektu klasy Result
    result_page = ResultPage(driver)

    # sprawdzenie, czy wyniki wyslwietlily sie na stronie
    results = result_page.get_results()
    assert len(results) > 0, "Niestety, nic nie ma"
