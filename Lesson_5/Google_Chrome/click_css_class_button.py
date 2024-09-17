from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()
    ))

# Открыть страницу
driver.get("http://uitestingplayground.com/classattr")

# Кликнуть на синюю кнопку
wait = WebDriverWait(driver, 10)
blue_button = wait.until(EC.element_to_be_clickable(
    driver.find_element(By.CSS_SELECTOR, '.btn-primary.btn-test')
    ))
blue_button.click()

sleep(5)
# Запустить скрипт 3 раза вручную, должен отработать одиноково
