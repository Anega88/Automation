from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()
    ))

# Открыть страницу
driver.get("http://uitestingplayground.com/dynamicid")

# Кликнуть на синюю кнопку
blue_button = driver.find_element(By.CLASS_NAME, 'btn-primary')
blue_button.click()

sleep(5)
# Запустить скрипт 3 раза вручную, должно отработать одинаково.
