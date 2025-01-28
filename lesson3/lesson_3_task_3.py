from address import Address
from mailing import Mailing

to_address = Address("675000", "Благовещенск", "Зейская", "317", "81")
from_address = Address("676630", "Екатеринославка", "Луговая", "1", "2")

mailing = Mailing(to_address, from_address, 250, "AB12345XY")

print(f"Отправление {mailing.track} из {mailing.from_address.postal_code}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в {mailing.to_address.postal_code}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")