from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
    )

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )
waiter = WebDriverWait(driver, 50)

clear_field = driver.find_element(By.CSS_SELECTOR, '#delay').clear()
sleep(2)
kye = driver.find_element(By.CSS_SELECTOR, '#delay').send_keys('45')

seven = driver.find_element(
    By.CSS_SELECTOR, 'span[class="btn btn-outline-primary"]'
    )
seven.click()
sleep(1)
plus = driver.find_element(
    By.CSS_SELECTOR, 'span[class="operator btn btn-outline-success"]'
    )
plus.click()
sleep(1)
eight = driver.find_element(
    By.XPATH, '(//span[@class="btn btn-outline-primary"])[2]'
    )
eight.click()
sleep(1)
equal = driver.find_element(
    By.CSS_SELECTOR, 'span[class="btn btn-outline-warning"]'
    )
equal.click()
sleep(1)

elem = waiter.until(EC.text_to_be_present_in_element(
    (By.CSS_SELECTOR, 'div[class="screen"]'), '15')
    )

assert elem, "Expected result '15' not found."

print('Correct result.')

driver.quit()
