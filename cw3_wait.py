from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# inicjalizacja przeglądarki Chrome
driver = webdriver.Chrome()

url = "https://www.w3schools.com/"

# upobranie konkretnego adresu w przeglarce
driver.get(url)

# rozmiar okna
driver.maximize_window()

# ciasteczka
time.sleep(5)
accept_cookies2 = driver.find_element("id", "accept-choices")
accept_cookies2.click()
# driver.find_element("id", "accept-choices").click()

#zatrzymanie skryptu
time.sleep(500)

# zamkniecie przegladarki
driver.quit()