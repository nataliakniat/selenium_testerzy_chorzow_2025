from joblib.testing import timeout
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def wait_for_button(driver, element_id):
    timeout = 10
    locator = ("id", element_id)

    locator_find = EC.visibility_of_element_located(locator)
    wait = WebDriverWait(driver, timeout, 0.5)

    return wait.until(locator_find,)

# inicjalizacja przeglądarki Chrome
driver = webdriver.Chrome()
url = "https://www.saucedemo.com/"

# upobranie konkretnego adresu w przeglarce
driver.get(url)

try:
    # sprawdzic, czy klawisz login jest widoczny
    login_button = wait_for_button(driver,"logi-button")
except TimeoutException:
    print("Nie znaleziono elementu")
else:
    print("Znaleziono")
    # kliknac ten przycisk TO DO
finally:
    # zatrzymanie skryptu
    time.sleep(5)
    # zamkniecie przegladarki
    driver.quit()



