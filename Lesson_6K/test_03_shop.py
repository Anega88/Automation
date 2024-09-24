from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
    )

driver.get("https://www.saucedemo.com/")
driver.implicitly_wait(20)

username = driver.find_element(By.CSS_SELECTOR, '#user-name')
username.send_keys('standard_user')

password = driver.find_element(By.CSS_SELECTOR, '#password')
password.send_keys('secret_sauce')
sleep(1)

login = driver.find_element(
    By.CSS_SELECTOR, '#login-button').click()
sleep(1)

take_1 = driver.find_element(
    By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack'
    ).click()
sleep(1)

take_2 = driver.find_element(
    By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt'
    ).click()
sleep(1)

take_3 = driver.find_element(
    By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie'
    ).click()
sleep(1)

shopping_cart = driver.find_element(
    By.CSS_SELECTOR, 'a[class="shopping_cart_link"]'
    ).click()
sleep(1)

checkout = driver.find_element(By.CSS_SELECTOR, '#checkout').click()
sleep(1)

first_name = driver.find_element(By.CSS_SELECTOR, '#first-name')
first_name.send_keys('Ekaterina')

last_name = driver.find_element(By.CSS_SELECTOR, '#last-name')
last_name.send_keys('Kolesnikova')

postal_code = driver.find_element(By.CSS_SELECTOR, '#postal-code')
postal_code.send_keys('053600')

button_continue = driver.find_element(By.CSS_SELECTOR, '#continue').click()
sleep(3)

total = driver.find_element(
    By.CSS_SELECTOR, 'div[class="summary_total_label"]'
    )

print(total.text)

driver.quit()
