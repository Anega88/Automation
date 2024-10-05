from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from Form import CheckZipCode


def test_full_fields_submit():
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()
        ))

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

    form.check_colors(colors)
    driver.quit()
