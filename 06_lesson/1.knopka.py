from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация WebDriver для Chrome
driver = webdriver.Chrome()

# Открыть страницу
driver.get("http://uitestingplayground.com/ajax")

# Найти синюю кнопку
blue_button = driver.find_element(By.CSS_SELECTOR, "button[class^='btn']")

# Нажать на синюю кнопку
blue_button.click()

# Дождаться появления зеленой плашки
green_message = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success"))
)

# Получить текст из зеленой плашки
print(green_message.text)

# Закрыть браузер
driver.quit()
