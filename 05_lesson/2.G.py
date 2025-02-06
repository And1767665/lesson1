from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация WebDriver для Google Chrome
driver = webdriver.Chrome()

# Открыть страницу с правильным URL
driver.get("http://uitestingplayground.com/classattr")

# Найти кнопку с нужным классом
blue_button = driver.find_element(By.CSS_SELECTOR, "button[class^='btn']")

# Кликнуть на кнопку (первый раз)
blue_button.click()

# Ожидание для пользователя перед вторым и третьим кликами
input("Нажмите Enter, чтобы кликнуть второй раз...")

# Кликнуть на кнопку (второй раз)
blue_button.click()

# Ожидание для пользователя перед третьим кликом
input("Нажмите Enter, чтобы кликнуть третий раз...")

# Кликнуть на кнопку (третий раз)
blue_button.click()

# Закрыть браузер
driver.quit()
