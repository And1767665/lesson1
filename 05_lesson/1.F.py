from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация WebDriver для Firefox
driver = webdriver.Firefox()

# Открыть страницу
driver.get("http://the-internet.herokuapp.com/entry_ad")

# Найти и кликнуть на кнопку Close в модальном окне
close_button = driver.find_element(By.XPATH, "//div[@class='modal-footer']/p/a")
close_button.click()

# Закрыть браузер
driver.quit()