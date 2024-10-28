from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import allure

from Shop import CheckTotalAmount


@allure.title("Заказ товаров на маркетплейсе")
@allure.description(
    "Добавление товаров в корзину, оформление заказа и сверка итоговой суммы заказа с ожидаемой суммой."
    )
@allure.feature("UPDATE")
@allure.severity("high")
@pytest.mark.tasks
def test_total_amount():
    with allure.step("Перейти на сайт."):
        assert True
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
            )
    with allure.step("Ввести логин и пароль, зайти в цчетную запись."):
        shop = CheckTotalAmount(driver)
        shop.log_in('standard_user', 'secret_sauce')
    with allure.step("Добавить товар в корзину."):
        shop.add_to_cart_and_checkout()
    with allure.step("Заполнить форму клиента."):
        shop.fill_in_form('Ekaterina', 'Kolesnikova', '053600')
    with allure.step("Сравнить итоговую сумму с ожидаемой."):
        shop.check_total_amount(58.29)
    driver.quit()
