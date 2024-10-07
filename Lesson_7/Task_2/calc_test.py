from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest

from Calc import CheckCalculator


@pytest.mark.tasks
def test_calculator():
    assert True
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
        )

    calc = CheckCalculator(driver)
    calc.clear_fill_in_field("45")
    calc.make_calculation()
    calc.check_result('15')
    driver.quit()
