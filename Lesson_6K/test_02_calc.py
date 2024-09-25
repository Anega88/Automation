from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )

    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
            )
        waiter = WebDriverWait(driver, 50)

        driver.find_element(By.CSS_SELECTOR, '#delay').clear()
        driver.find_element(By.CSS_SELECTOR, '#delay').send_keys('45')

        driver.find_element(
            By.CSS_SELECTOR, 'span[class="btn btn-outline-primary"]'
            ).click()
        driver.find_element(
            By.CSS_SELECTOR, 'span[class="operator btn btn-outline-success"]'
            ).click()
        driver.find_element(
            By.XPATH, '(//span[@class="btn btn-outline-primary"])[2]'
            ).click()
        driver.find_element(
            By.CSS_SELECTOR, 'span[class="btn btn-outline-warning"]'
            ).click()

        elem = waiter.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, 'div[class="screen"]'), '15')
        )

        assert elem, "Expected result '15' not found."
        print('Correct result.')

    finally:
        driver.quit()
