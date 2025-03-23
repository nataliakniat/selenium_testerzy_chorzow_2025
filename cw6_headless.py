from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
import os

# konfigurajca przegladarki
chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)

url = "https://www.timeanddate.com/worldclock/"
driver.get(url)

# czekamy na tabele
#/html/body/div[5]/section[1]/div/section/div[1]/div/table
wait = WebDriverWait(driver, 10, 0.5)
wait.until(EC.presence_of_all_elements_located((By.XPATH, '//table[contains(@class, "zebra")]')))

rows = driver.find_elements(By.XPATH, '//table[contains(@class, "zebra")]')

print(len(rows))

driver.quit()