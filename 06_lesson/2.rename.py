from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация WebDriver для Chrome
driver = webdriver.Chrome()

# Открыть страницу
driver.get("http://uitestingplayground.com/textinput")

# Найти поле ввода и ввести текст SkyPro
input_field = driver.find_element(By.ID, "newButtonName")
input_field.send_keys("SkyPro")

# Найти синюю кнопку и кликнуть на нее
submit_button = driver.find_element(By.CSS_SELECTOR, "button[class^='btn']")
submit_button.click()

# Получить текст кнопки
button_text = submit_button.text

# Вывести текст кнопки
print(button_text)

# Закрыть браузер
driver.quit()
