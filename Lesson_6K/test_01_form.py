from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
    )

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
waiter = WebDriverWait(driver, 20)

fields = {
    'first-name': 'Иван',
    'last-name': 'Петров',
    'address': 'Ленина, 55-3',
    'e-mail': 'test@skypro.com',
    'phone': '+7985899998787',
    'city': 'Москва',
    'country': 'Россия',
    'job-position': 'QA',
    'company': 'SkyPro'
}

for field, value in fields.items():
    elem = waiter.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, f'input[name="{field}"]')
        ))
    elem.send_keys(value)

button_submit = waiter.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
    )
button_submit.click()

color_zip_code = waiter.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, '#zip-code')
    )).value_of_css_property("background-color")

color_first_name = waiter.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, '#first-name')
    )).value_of_css_property("background-color")

color_last_name = waiter.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, '#last-name')
    )).value_of_css_property("background-color")

color_address = waiter.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, '#address')
    )).value_of_css_property("background-color")

color_phone_number = waiter.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, '#phone')
    )).value_of_css_property("background-color")

color_email = waiter.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, '#e-mail')
    )).value_of_css_property("background-color")

color_city = waiter.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, '#city')
    )).value_of_css_property("background-color")

color_country = waiter.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, '#country')
    )).value_of_css_property("background-color")

color_job_position = waiter.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, '#job-position')
    )).value_of_css_property("background-color")

color_company = waiter.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, '#company')
    )).value_of_css_property("background-color")

assert color_zip_code == 'rgba(248, 215, 218, 1)'

assert color_first_name == 'rgba(209, 231, 221, 1)'
assert color_last_name == 'rgba(209, 231, 221, 1)'
assert color_address == 'rgba(209, 231, 221, 1)'
assert color_email == 'rgba(209, 231, 221, 1)'
assert color_phone_number == 'rgba(209, 231, 221, 1)'
assert color_city == 'rgba(209, 231, 221, 1)'
assert color_country == 'rgba(209, 231, 221, 1)'
assert color_job_position == 'rgba(209, 231, 221, 1)'
assert color_company == 'rgba(209, 231, 221, 1)'

print('All color checks passed.')


driver.quit()
