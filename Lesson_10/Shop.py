from selenium.webdriver.common.by import By
import allure


class CheckTotalAmount:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    @allure.step("Ввести логин и пароль, залогиниться.")
    def log_in(self, username: str, password: str) -> str:
        """
        Функция, которая вводит логин и пароль, после чего логинится в систему.
        """
        user = self._driver.find_element(By.CSS_SELECTOR, '#user-name')
        user.send_keys(username)

        pasw = self._driver.find_element(
            By.CSS_SELECTOR, '#password'
            )
        pasw.send_keys(password)

        self._driver.find_element(By.CSS_SELECTOR, '#login-button').click()

    @allure.step("Добавить товар в корзину.")
    def add_to_cart_and_checkout(self):
        """
        Функция находит необходимый товар и добавляет его в корзину.
        Переходит в корзину для оформленяи заказа.
        """
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

    @allure.step("Заполнить форму клиента.")
    def fill_in_form(self, first_name: str, last_name: str, postal_code: int):
        """
        Эта функция заполняет данные покупателяи и почтовый индекс.
        """
        self._driver.find_element(
            By.CSS_SELECTOR, '#first-name').send_keys(first_name)
        self._driver.find_element(
            By.CSS_SELECTOR, '#last-name'
            ).send_keys(last_name)
        self._driver.find_element(
            By.CSS_SELECTOR, '#postal-code'
            ).send_keys(postal_code)
        self._driver.find_element(By.CSS_SELECTOR, '#continue').click()

    @allure.step("Сверить ожидаемую итоговую сумму с фактической.")
    def check_total_amount(self, expected: int) -> int:
        """
        Функция выводит итоговую сумму заказа и
        сверяет ее с ожидаемым результатом.
        """
        total = self._driver.find_element(
            By.CSS_SELECTOR, 'div[class="summary_total_label"]'
            )
        total_text = total.text
        total_amount = float(total_text.replace("Total: $", ""))
        assert total_amount == expected, f"Expected total {expected}, but got {total_amount}"
