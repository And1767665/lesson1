from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация WebDriver для Chrome
driver = webdriver.Chrome()

# Открыть страницу
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/"
    "loading-images.html"
)

# Дождаться, пока все изображения будут видимыми
WebDriverWait(driver, 30).until(
    EC.visibility_of_all_elements_located((By.TAG_NAME, "img"))
)

# Найти все изображения на странице
images = driver.find_elements(By.TAG_NAME, "img")

# Убедиться, что на странице есть хотя бы три изображения
if len(images) >= 3:
    # Получить атрибут src третьей картинки
    third_image_src = images[2].get_attribute("src")
    print(third_image_src)
else:
    print("Меньше 3 изображений на странице.")

# Закрыть браузер
driver.quit()
