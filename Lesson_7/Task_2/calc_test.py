from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from Calc import CheckCalculator


def test_calculator():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
        )

    calc = CheckCalculator(driver)
    calc.clear_fill_in_fuild("45")
    calc.make_calculation()
    calc.check_result('15')
    driver.quit()
