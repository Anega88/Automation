from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckZipCode:
   
    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
            )
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()


    def fill_in_fields_and_submit(
            self, first_name, last_name,
            address, email, phone, city,
            country, job_position, company):
        waiter = WebDriverWait(self._driver, 20)

        fields = {
            'first-name': first_name,
            'last-name': last_name,
            'address': address,
            'e-mail': email,
            'phone': phone,
            'city': city,
            'country': country,
            'job-position': job_position,
            'company': company
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
   
    def zip_code_color(self, zip_code, first_name, last_name,
                       address, email, phone, city,
                       country, job_position, company):
        WebDriverWait(self._driver, 20)
        {
            'zip-code': zip_code,
            'first-name': first_name,
            'last-name': last_name,
            'address': address,
            'phone': email,
            'e-mail': phone,
            'city': city,
            'country': country,
            'job-position': job_position,
            'company': company
        }
   
    def check_colors(self, colors):
        waiter = WebDriverWait(self._driver, 20)
        for field, expected_color in colors.items():
            elem = waiter.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, f'#{field}')
                ))
            color = elem.value_of_css_property("background-color")
            assert color == expected_color, f"Color for {field} is {color}, expected {expected_color}"
        print('All color checks passed.')
