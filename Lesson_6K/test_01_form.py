import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_field_colors():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )

    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
            )
        waiter = WebDriverWait(driver, 20)

        fields = {
            'first-name': 'Иван',
            'last-name': 'Петров',
            'address': 'Ленина, 55-3',
            'e-mail': 'test@skypro.com',
            'phone': '+7985899998787',
            'city': 'Москва',
            'country': 'Россия',
            'job-position': 'QA',
            'company': 'SkyPro'
        }

        for field, value in fields.items():
            elem = waiter.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, f'input[name="{field}"]')
            ))
            elem.send_keys(value)

        button_submit = waiter.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'button[type="submit"]')
            ))
        button_submit.click()

        colors = {
            'zip-code': 'rgba(248, 215, 218, 1)',
            'first-name': 'rgba(209, 231, 221, 1)',
            'last-name': 'rgba(209, 231, 221, 1)',
            'address': 'rgba(209, 231, 221, 1)',
            'phone': 'rgba(209, 231, 221, 1)',
            'e-mail': 'rgba(209, 231, 221, 1)',
            'city': 'rgba(209, 231, 221, 1)',
            'country': 'rgba(209, 231, 221, 1)',
            'job-position': 'rgba(209, 231, 221, 1)',
            'company': 'rgba(209, 231, 221, 1)'
        }

        for field, expected_color in colors.items():
            elem = waiter.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, f'#{field}')
            ))
            color = elem.value_of_css_property("background-color")
            assert color == expected_color, f"Color for {
                field} is {color}, expected {expected_color}"

        print('All color checks passed.')

    finally:
        driver.quit()
