from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
    )

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )

waiter = WebDriverWait(driver, 40)
picture = waiter.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#award'))
    )

link = picture.get_attribute('src')

print(link)

driver.quit()
