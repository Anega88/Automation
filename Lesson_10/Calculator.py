from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CheckCalculator:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
            )
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    @allure.step(
            "Очистить поле задержки сайта и ввести необходимое время задержки."
            )
    def clear_fill_in_field(self, time: int) -> int:
        """
        Эта функция очищает поле time и вводит
        в него количество сеекунд задержки действия.
        """
        self._driver.find_element(By.CSS_SELECTOR, '#delay').clear()
        self._driver.find_element(By.CSS_SELECTOR, '#delay').send_keys(time)

    @allure.step("Ввести пример в калькулятор '8 + 7 ='")
    def make_calculation(self):
        """
        Эта функция вводит пример '8 + 7 ='.
        """
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

    @allure.step("Сверить ожидаемый результат и фактический.")
    def check_result(self, result: int) -> int:
        """
        Эта функция проверяет результат,
        который должен равняться 15 по условиям задачи.
        """
        waiter = WebDriverWait(self._driver, 50)
        elem = waiter.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, 'div[class="screen"]'), result)
        )

        assert elem, "Expected result '15' not found."
        print('Correct result.')
