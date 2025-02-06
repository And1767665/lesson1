from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация WebDriver для Firefox
driver = webdriver.Firefox()

# Открыть страницу
driver.get("http://the-internet.herokuapp.com/inputs")

# Найти поле ввода
input_field = driver.find_element(By.TAG_NAME, "input")

# Ввести 1000
input_field.send_keys("1000")

# Очистить поле
input_field.clear()

# Ввести 999
input_field.send_keys("999")

# Закрыть браузер
driver.quit()
