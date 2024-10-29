from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import allure


from Calculator import CheckCalculator


@allure.title("Корректность рассчетов калькулятора")
@allure.description("Ввод примера '8+7=' и сверка с ожидаемым результатом.")
@allure.feature("UPDATE")
@allure.severity("high")
@pytest.mark.tasks
def test_calculator():
    with allure.step("Перейти на сайт."):
        assert True
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
            )
    with allure.step("Ввести время задержки сайта."):
        calc = CheckCalculator(driver)
        calc.clear_fill_in_field("45")
    with allure.step("Ввести пример '8+7=' на калькуляторе."):
        calc.make_calculation()
    with allure.step("Сравнить фактический результат и ожидаемый."):
        calc.check_result('15')
    driver.quit()
