from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=FirefoxService(
    GeckoDriverManager().install()
    ), options=options)

# Открыть сайт
driver.get('https://the-internet.herokuapp.com/inputs')

# Ввести в поле текст 1000
sleep(1)
input_field = driver.find_element(By.TAG_NAME, 'input')
input_field.send_keys("1000")
sleep(2)

# Очистить поле
input_field.clear()
sleep(1)

# Ввести в поле текст 999
input_field.send_keys("999")

sleep(3)

driver.quit()
