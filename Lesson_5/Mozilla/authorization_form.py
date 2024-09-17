from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=FirefoxService(
    GeckoDriverManager().install()
    ), options=options)

# Открыть сайт.
driver.get('https://the-internet.herokuapp.com/login')
sleep(1)

# В поле Username ввести значение.
username = driver.find_element(By.ID, 'username').send_keys("tomsmith")
sleep(2)

# В поле Password ввести значение.
password = driver.find_element(By.ID, 'password').send_keys("SuperSecretPassword!")
sleep(2)

# Нажать кнопку Login.
login = driver.find_element(By.CSS_SELECTOR, 'button.radius')
login.click()
sleep(2)

driver.quit()
