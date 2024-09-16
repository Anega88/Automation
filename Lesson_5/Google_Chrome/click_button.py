from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()
    ))

# Открыть страницу
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Пять раз кликнуть на кнопку Add element
wait = WebDriverWait(driver, 10)
add_button = wait.until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, 'button[onclick="addElement()"]')
    ))

for _ in range(5):
    add_button.click()
    sleep(1)

# Собрать со страницы список кнопок Delete
buttons_delete = driver.find_elements(
    By.CSS_SELECTOR, 'button[onclick="deleteElement()"]'
    )

for button_delete in buttons_delete:
    print(button_delete.text)

# Вывести на экран размер списка
print(f'Количество кнопок Delete: {len(buttons_delete)}')

sleep(20)

driver.quit()
