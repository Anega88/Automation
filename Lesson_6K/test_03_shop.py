from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def test_sauce_demo_checkout():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )

    try:
        driver.get("https://www.saucedemo.com/")
        driver.implicitly_wait(20)

        username = driver.find_element(By.CSS_SELECTOR, '#user-name')
        username.send_keys('standard_user')

        password = driver.find_element(
            By.CSS_SELECTOR, '#password'
            )
        password.send_keys('secret_sauce')
        driver.find_element(By.CSS_SELECTOR, '#login-button').click()

        driver.find_element(
            By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack'
            ).click()
        driver.find_element(
            By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt'
            ).click()
        driver.find_element(
            By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie'
            ).click()
        driver.find_element(
            By.CSS_SELECTOR, 'a[class="shopping_cart_link"]'
            ).click()
        driver.find_element(By.CSS_SELECTOR, '#checkout').click()
        
        driver.find_element(
            By.CSS_SELECTOR, '#first-name').send_keys('Ekaterina')
        driver.find_element(
            By.CSS_SELECTOR, '#last-name'
            ).send_keys('Kolesnikova')
        driver.find_element(
            By.CSS_SELECTOR, '#postal-code'
            ).send_keys('053600')
        driver.find_element(By.CSS_SELECTOR, '#continue').click()
        
        total = driver.find_element(
            By.CSS_SELECTOR, 'div[class="summary_total_label"]'
            )
        print(total.text)
        assert "Total: $" in total.text, "Total amount text not found"
    finally:
        driver.quit()
