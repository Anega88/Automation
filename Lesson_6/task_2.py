from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
    )

driver.get("http://uitestingplayground.com/textinput")

kye = driver.find_element(
    By.CSS_SELECTOR, '#newButtonName').send_keys("SkyPro")

button = driver.find_element(By.CSS_SELECTOR, '#updatingButton').click()

waiter = WebDriverWait(driver, 20)
change_button = waiter.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#updatingButton'))
    )

button = driver.find_element(By.CSS_SELECTOR, '#updatingButton')

text_button = change_button.text

print(text_button)

driver.quit()
