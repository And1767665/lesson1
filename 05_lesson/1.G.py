from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация WebDriver для Google Chrome
driver = webdriver.Chrome()

# Открыть страницу
driver.get("http://uitestingplayground.com/dynamicid")

# Кликнуть на синюю кнопку (первый раз)
blue_button = driver.find_element(By.CSS_SELECTOR, "button[class^='btn']")
blue_button.click()

# Ожидание для пользователя перед вторым и третьим кликами
input("Нажмите Enter, чтобы кликнуть второй раз...")

# Кликнуть на синюю кнопку (второй раз)
blue_button.click()

# Ожидание для пользователя перед третьим кликом
input("Нажмите Enter, чтобы кликнуть третий раз...")

# Кликнуть на синюю кнопку (третий раз)
blue_button.click()

# Закрыть браузер
driver.quit()
