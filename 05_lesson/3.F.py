from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация WebDriver для Firefox
driver = webdriver.Firefox()

# Открыть страницу
driver.get("http://the-internet.herokuapp.com/login")

# Найти поля ввода и кнопку
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

# Ввести данные и нажать Login
username_field.send_keys("tomsmith")
password_field.send_keys("SuperSecretPassword!")
login_button.click()

# Закрыть браузер
driver.quit()
