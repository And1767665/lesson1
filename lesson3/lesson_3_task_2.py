from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 13", "+79161234567"),
    Smartphone("Samsung", "Galaxy S21", "+79263456789"),
    Smartphone("Google", "Pixel 6", "+79374567890"),
    Smartphone("Xiaomi", "Redmi Note 11", "+79485678901"),
    Smartphone("OnePlus", "9 Pro", "+79596789012")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.phone_number}")