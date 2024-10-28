from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import allure


from FormZipCode import CheckZipCode


@allure.title("Критичность пустого поля Индекс")
@allure.description("Поле индекс оставляем пустым при заполнении формы")
@allure.feature("CREATE")
@allure.severity("high")
@pytest.mark.tasks
def test_full_fields_submit():
    with allure.step("Перейти на сайт."):
        assert True
        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()
            ))

    with allure.step("Заполнить форму клиента."):
        form = CheckZipCode(driver)
        form.fill_in_fields_and_submit(
            "Иван", "Петров", "Ленина, 55-3",
            "test@skypro.com", "+7985899998787",
            "Москва", "Россия", "QA", "SkyPro"
            )

    colors = {
        'zip-code': 'rgba(248, 215, 218, 1)',
        'first-name': 'rgba(209, 231, 221, 1)',
        'last-name': 'rgba(209, 231, 221, 1)',
        'address': 'rgba(209, 231, 221, 1)',
        'e-mail': 'rgba(209, 231, 221, 1)',
        'phone': 'rgba(209, 231, 221, 1)',
        'city': 'rgba(209, 231, 221, 1)',
        'country': 'rgba(209, 231, 221, 1)',
        'job-position': 'rgba(209, 231, 221, 1)',
        'company': 'rgba(209, 231, 221, 1)'
    }
    with allure.step("Проверить, что заполненные поля подсвечены зеленым, а поле Индекс подсвечено красным."):
        form.check_colors(colors)
        driver.quit()
