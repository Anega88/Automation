from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=FirefoxService(
    GeckoDriverManager().install()
    ), options=options)

# Открыть сайт
driver.get('http://the-internet.herokuapp.com/entry_ad')

# Нажать кнопку Close
wait = WebDriverWait(driver, 10)
button_close = wait.until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, '.modal-footer')
    ))
sleep(2)
button_close.click()

sleep(5)

driver.quit()
