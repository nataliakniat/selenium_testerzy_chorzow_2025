from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# inicjalizacja przeglądarki Chrome
driver = webdriver.Chrome()

# implicitly wait - oczekiwanie na pojawie się każdego elementu na stronie przez maksymanie X (podajemy jako parametr) sekund
driver.implicitly_wait(5)

url = "https://www.w3schools.com/"

# upobranie konkretnego adresu w przeglarce
driver.get(url)

# rozmiar okna
driver.maximize_window()

# ciasteczka
accept_cookies2 = driver.find_element("id", "accept-choices")
accept_cookies2.click()
# driver.find_element("id", "accept-choices").click()

# Tutorials
menu = driver.find_element("id", "navbtn_tutorials")
menu.click()
#webdriver.ActionChains(driver).move_to_element(menu).click().perform()

# learn HTML
learnHTML = driver.find_element('xpath', '//*[@id="tutorials_html_css_links_list"]/div[1]/a[1]')
#learnHTML = driver.find_element('xpath', '//a[@title="HTML Tutorial"]')
learnHTML.click()

#zatrzymanie skryptu
time.sleep(500)

# zamkniecie przegladarki
driver.quit()