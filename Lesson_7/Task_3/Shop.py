from selenium.webdriver.common.by import By
import pytest

class CheckTotalAmount:
 
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def log_in(self, username, password):
        user = self._driver.find_element(By.CSS_SELECTOR, '#user-name')
        user.send_keys(username)

        pasw = self._driver.find_element(
            By.CSS_SELECTOR, '#password'
            )
        pasw.send_keys(password)

        self._driver.find_element(By.CSS_SELECTOR, '#login-button').click()
   
    def add_to_cart_and_checkout(self):
        self._driver.find_element(
            By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack'
            ).click()
        self._driver.find_element(
            By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt'
            ).click()
        self._driver.find_element(
            By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie'
            ).click()
        self._driver.find_element(
            By.CSS_SELECTOR, 'a[class="shopping_cart_link"]'
            ).click()
        self._driver.find_element(By.CSS_SELECTOR, '#checkout').click()

    def fill_in_form(self, first_name, last_name, postal_code):
        self._driver.find_element(
            By.CSS_SELECTOR, '#first-name').send_keys(first_name)
        self._driver.find_element(
            By.CSS_SELECTOR, '#last-name'
            ).send_keys(last_name)
        self._driver.find_element(
            By.CSS_SELECTOR, '#postal-code'
            ).send_keys(postal_code)
        self._driver.find_element(By.CSS_SELECTOR, '#continue').click()

    def check_total_amount(self, expected):
        total = self._driver.find_element(
            By.CSS_SELECTOR, 'div[class="summary_total_label"]'
            )
        total_text = total.text
        total_amount = float(total_text.replace("Total: $", ""))
        assert total_amount == expected, f"Expected total {expected}, but got
        {total_amount}"
