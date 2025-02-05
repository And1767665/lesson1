from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация WebDriver для Google Chrome
driver = webdriver.Chrome()

# Открыть страницу
driver.get("http://uitestingplayground.com/dynamicid")

# Кликнуть на синюю кнопку три раза
blue_button = driver.find_element(By.CSS_SELECTOR, "button[class^='btn']")
for _ in range(3):
    blue_button.click()

# Закрыть браузер
driver.quit()