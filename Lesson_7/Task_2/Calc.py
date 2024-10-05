from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckCalculator:
   
    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
            )
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()
    
    def clear_fill_in_fuild(self, time):
        self._driver.find_element(By.CSS_SELECTOR, '#delay').clear()
        self._driver.find_element(By.CSS_SELECTOR, '#delay').send_keys(time)
  
    def make_calculation(self):
        self._driver.find_element(
            By.CSS_SELECTOR, 'span[class="btn btn-outline-primary"]'
            ).click()
        self._driver.find_element(
            By.CSS_SELECTOR, 'span[class="operator btn btn-outline-success"]'
            ).click()
        self._driver.find_element(
            By.XPATH, '(//span[@class="btn btn-outline-primary"])[2]'
            ).click()
        self._driver.find_element(
            By.CSS_SELECTOR, 'span[class="btn btn-outline-warning"]'
            ).click()
    
    def check_result(self, result):
        waiter = WebDriverWait(self._driver, 50)
        elem = waiter.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, 'div[class="screen"]'), result)
        )

        assert elem, "Expected result '15' not found."
        print('Correct result.')
